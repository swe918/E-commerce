import pandas as pd  # Using Pandas for data cleaning
import plotly.express as px  # Using Plotly for graphs
import plotly.graph_objects as go  # Advanced and customized graphs
import plotly.io as pio  # For customizing graph templates
import plotly.colors as colors  # For color palettes

# Setting default template for Plotly
pio.templates.default = 'plotly_white'

# Load dataset with error handlingimport pandas as pd  # USING PANDAS FOR DATA CLEANING

Data= pd.read_csv(r'C:\Users\HP\Desktop\E-commerce\Sample - Superstore (1).csv', encoding="latin-1")
print(Data.head())

print(Data.describe())# USED FOR DESCRIPTIVE STATISTICS 

print(Data.info()) # Show data types and missing values
# CONVERTING DATE COLUMN
Data["Order Date"]=pd.to_datetime(Data["Order Date"])
print(Data.info())

Data["Ship Date"]=pd.to_datetime(Data["Ship Date"])
print(Data.info())
# CREATING NEW COLUMN FOR ANALYSIS
Data["Order Month"]= Data["Order Date"].dt.month
Data["Order Year"]=Data["Order Date"].dt.year
Data["Order day of week"]=Data["Order Date"].dt.day_of_week
print(Data.head(10))

# MONTHLY SALES ANALYSIS
sales_by_month=Data.groupby("Order Month")["Sales"].sum().reset_index()
fig=px.line(sales_by_month,
            x="Order Month",
            y="Sales",
            title="Monthly Sales Analysis")
fig.show()

# SALES BY CATEGORY
print(Data.head())
print(Data["Category"])
sales_by_category=Data.groupby("Category")["Sales"].sum().reset_index()
print(sales_by_category)
fig1=px.bar(sales_by_category,
            x="Category",
            y="Sales",
            title="OVERALL SALES BY CATEGORY")
fig1.show()
fig=px.pie(sales_by_category,
          values="Sales",
          names="Category",
          hole=0.2,
          color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition="inside",textinfo="percent+label")
fig.update_layout(title_text="Analysis Of Sales With Category", title_font=dict(size=24))
fig.show()
# SALES BY SUB- CATEGORY
sales_by_subcat=Data.groupby("Sub-Category")["Sales"].sum().reset_index()
print(sales_by_subcat)
fig=px.bar(sales_by_subcat,
           x="Sub-Category",
           y="Sales",
           title="Sales Analysis By Sub-Category")
fig.show()

# PROFIT BY MONTH
monthly_profit=Data.groupby("Order Month")["Profit"].sum().reset_index()
fig=px.line(monthly_profit,
            x="Order Month",
            y="Profit",
            title="Monthly Profit")
fig.show()
# PROFIT BY CATEGORY
p_by_category=Data.groupby("Category")["Profit"].sum().reset_index()
print(p_by_category)
fig=px.pie(p_by_category,
          values="Profit",
          names="Category",
          hole=0.5,
          color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition="inside",textinfo="percent+label")
fig.update_layout(title_text="Analysis Of Profit With Category", title_font=dict(size=24))
fig.show()
# PROFIT BY SUB-CATEGORY
p_by_sub_cat=Data.groupby("Sub-Category")["Profit"].sum().reset_index()
fig=px.bar(p_by_sub_cat,
           x="Sub-Category",
           y="Profit",
           title="Profit Analysis By Sub-Category")
fig.show()
# Sales And Profit Analysis By Customer Segmen
sales_profit_by_seg=Data.groupby("Segment").agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
print(sales_profit_by_seg)

color_palette=colors.qualitative.Pastel
fig=go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_seg["Segment"],
                     y=sales_profit_by_seg["Sales"],
                     name="Sales",
                     marker_color=color_palette[0]
              ))

fig.add_trace(go.Bar(x=sales_profit_by_seg["Segment"],
                     y=sales_profit_by_seg["Profit"],
                     name="Profit",
                     marker_color=color_palette[1]
              ))
fig.update_layout(title="Sales And Profit Analysis By Customer Segment", xaxis_title="Customer Segment", yaxis_title="Amount")
fig.show()

# SALES TO PROFIT RATIO
sales_profit_by_seg=Data.groupby("Segment").agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
sales_profit_by_seg["sales to profit ratio"]=sales_profit_by_seg["Sales"]/sales_profit_by_seg["Profit"]
print(sales_profit_by_seg[["Segment","sales to profit ratio"]])