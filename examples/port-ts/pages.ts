import * as port from "@port-labs/port";
import * as fs from "fs"; // Assuming we use Node's 'fs' module for file reading

// ------------------ Widget Helper Functions ------------------ 

interface WidgetConfig { // Sample interface, adjust as needed
    id: string;
    title: string;
    type: string;
    icon?: string; // Optional properties
    description?: string;
    markdown?: string;
    blueprint?: string;
    displayMode?: string;
    dataset?: any;
    excludedFields?: string[];
    property?: string;
    calculationBy?: string;
    urlType?: string;
    // ... other widget properties
}

function generateWidgetId(title: string, widgetType: string): string {
    const titleWords = title.split(" ");
    const camelCaseTitle = titleWords[0].toLowerCase() + titleWords.slice(1).map(word => word).join("");
    const baseId = `${camelCaseTitle}${widgetType}`;

    // Ensure the length does not exceed the limit
    const maxLength = 20; // Replace with the correct limit if needed
    return baseId.substring(0, maxLength);
}

function createMarkdownWidget(title: string, description: string, markdownContent: string): [WidgetConfig, string] {
    const widgetId = generateWidgetId(title, "markdown");
    const widgetConfig: WidgetConfig = {
        title,
        icon: "BlankPage",
        markdown: markdownContent,
        type: "markdown",
        description,
        id: widgetId,
    };
    return [widgetConfig, widgetId];
}


function createTableExplorerWidget(title: string, dataset: any, excludedFields: string[] = ["properties.readme"]): [WidgetConfig, string] {
    const widgetId = generateWidgetId(title, "table-entities-explorer");
    const widgetConfig: WidgetConfig = {
        displayMode: "widget", // Assuming  this property exists
        title,
        type: "table-entities-explorer",
        dataset,
        id: widgetId,
        excludedFields,
    };
    return [widgetConfig, widgetId];
}

function createEntitiesPieChartWidget(title: string, dataset: any, property: string): [WidgetConfig, string] {
    const widgetId = generateWidgetId(title, "entities-pie-chart");
    const widgetConfig = {
        title,
        icon: "PieChart", 
        type: "entities-pie-chart",
        dataset,
        property, 
        id: widgetId,
    };
    return [widgetConfig, widgetId];
}

function createIframeWidget(title: string, url: string, urlType: string = "public", description: string = ""): [WidgetConfig, string] {
    const widgetId = generateWidgetId(title, "iframe-widget");
    const widgetConfig = {
        title,
        description,
        icon: "Code", 
        urlType,
        url,
        type: "iframe-widget",
        id: widgetId,
    };
    return [widgetConfig, widgetId];
}

function createEntitiesNumberChartWidget(
    title: string,
    blueprintId: string,
    dataset: any = [],
    func: "average" | "count" | "sum" = "average",
    measureTimeBy: string = "$createdAt",
    averageOf: "day" | "week" | "month" = "day",
    description: string = ""
): [WidgetConfig, string] {
    const widgetId = generateWidgetId(title, "entities-number-chart");
    const widgetConfig = {
        blueprint: blueprintId, 
        calculationBy: "entities", 
        title,
        description,
        type: "entities-number-chart",
        icon: "Calculator", 
        dataset,
        func,
        measureTimeBy,
        averageOf,
        unit: "custom", 
        unitCustom: "per day", 
        id: widgetId,
    };
    return [widgetConfig, widgetId];
}

// ... Similar functions for other widget types:  create_table_explorer_widget, create_entities_pie_chart_widget, etc.

// ------------------ Other Helper Functions ------------------ 

function readMarkdownFile(filePath: string): string {
    return fs.readFileSync(filePath, "utf-8");
}

function useDataset(blueprintId: string): any { // Type may vary depending on your provider
    return {
        combinator: "and",
        rules: [{ "operator": "=", "value": blueprintId, "property": "$blueprint" }],
    };
}

// ------------------ Sample Data & Widget Creation ------------------ 

const servicesDataset = useDataset("service");
const githubPrDataset = useDataset("githubPullRequest");

const filePath = "microservices.md";
const markdownContent = readMarkdownFile(filePath);

const [markdownConfig, markdownId] = createMarkdownWidget(
    "Service Guide",
    "Services are typically organized around business capabilities...",
    markdownContent
);

// Table Explorer Widget
const [tableConfig, tableId] = createTableExplorerWidget(
    "Services", 
    servicesDataset, 
    ["properties.readme", "properties.slack"] 
);

// Entities Pie Chart Widget
const [pieChartConfig, pieChartId] = createEntitiesPieChartWidget(
    "Languages", 
    servicesDataset, 
    "property#language" 
);

// Iframe Widget
const [quoteConfig, quoteId] = createIframeWidget(
    "Quote of the Day", 
    "https://kwize.com/quote-of-the-day/embed/&txt=0" 
);

// Entities Number Chart Widget
const [prChartConfig, prChartId] = createEntitiesNumberChartWidget(
    "Avg Pull Requests",
    "githubPullRequest", 
    githubPrDataset, 
    "average", 
    "$createdAt",
    "day",
    "How many PRs do we open daily?" 
);

// ------------------ Dashboard Layout ------------------ 

const dashboardLayout = {
    id: "myDashboardWidget", // Optional
    type: "dashboard-widget",
    layout: [
        { 
            // Row 1
            columns: [
                { id: markdownId, size: 6 }, // Markdown Widget (half width)
                { id: pieChartId, size: 6 }, // Pie Chart Widget (half width)
            ],
            height: 400 
        },
        {
            // Row 2
            columns: [
                { id: quoteId, size: 12 },   // Quote Widget (half width)
                // { id: prChartId, size: 6 }, // PR Chart Widget (half width)
            ],
            height: 400 
        },
        { 
            // Row 3
            columns: [
                { id: tableId, size: 12 }   // Table Widget (full width)
            ],
            height: 400 
        }
    ]
};

const widgetsConfig = {
    ...dashboardLayout,
    widgets: [
        markdownConfig,
        pieChartConfig,
        quoteConfig,
        // prChartConfig,
        tableConfig 
    ]
};

// ------------------ Page Creation ------------------ 

export const microserviceDashboardPage = new port.Page(
    "microservice-overview-page-resource",
    {
        identifier: "microservice_overview_page",
        title: "Microservices Dashboard",
        icon: "Microservice",
        type: "dashboard",
        widgets: [JSON.stringify(widgetsConfig)] // May need adjustment 
    }
);
