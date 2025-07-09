import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="IFAMA Ireland 2026 Insights Dashboard - Simulation Model", layout="wide")

st.title("Ireland 2026: Agriculture & Food System Innovations - Simulation Prototype")
st.markdown("""
Welcome to the Ireland's insights dashboard. This interactive app showcases the key themes that will define Ireland's agricultural transformation leading into 2026.
""")

# Helper function for crosshair-like hover
crosshair_template = "<b>%{x}</b><br>%{y}<extra></extra>"

# Agricultural Products and Organizations Overview
st.header("Irish Agri-Food Landscape")
products_data = pd.DataFrame({
    'Product': [
        'Beef', 'Dairy (Butter, Cheese, Milk)', 'Barley', 'Wheat', 'Oats', 'Potatoes', 'Lamb', 'Pork',
        'Seafood (Salmon, Oysters)', 'Apples', 'Mushrooms', 'Honey'
    ],
    'Export Value (€M, est.)': [2100, 5200, 340, 200, 85, 170, 290, 320, 450, 60, 120, 45]
})
fig0 = px.bar(products_data, x='Product', y='Export Value (€M, est.)',
              title='Top Agri-Food Products Exported by Ireland')
fig0.update_traces(hovertemplate=crosshair_template)
st.plotly_chart(fig0, use_container_width=True)
st.info("This bar chart highlights Ireland’s dominant agri-food exports, with dairy leading the market, followed by beef and seafood. It showcases product-specific value contributions to the national economy.")

# Key Irish Agri-Food Organizations
st.subheader("Key Organizations in Ireland")
st.markdown("""
- **Teagasc** – Agriculture and Food Development Authority
- **Bord Bia** – Irish Food Board
- **Bord Iascaigh Mhara (BIM)** – Irish Sea Fisheries Board
- **Department of Agriculture, Food and the Marine (DAFM)**
- **Enterprise Ireland** – Agri-innovation and exports
- **Macra na Feirme** – Young farmer development
- **AgriAware** – Education and public engagement
- **Irish Farmers’ Association (IFA)** – National representation
- **Irish Organic Association** – Organic standards
- **UCC, UCD, TCD Agri-Food Research Centres** – Innovation and sustainability
""")

# Theme 1: Sustainable Intensification
st.header("1. Sustainable Intensification")
sust_data = pd.DataFrame({
    'Farm': ['Glanbia Ireland', 'Dairygold Co-op'],
    'Carbon Offset (tons)': [290000, 310000],
    'Regenerative Practices (%)': [72, 78]
})
fig1 = px.bar(sust_data, x='Farm', y='Carbon Offset (tons)', color='Regenerative Practices (%)',
              title='Carbon-Neutral Farming & Regenerative Agriculture in Ireland')
fig1.update_traces(hovertemplate=crosshair_template)
st.plotly_chart(fig1, use_container_width=True)
st.info("Dairygold and Glanbia illustrate Ireland’s dual approach to productivity and sustainability, with high carbon offset values and impressive adoption of regenerative practices.")

# Theme 2: AgTech Revolution
st.header("2. AgTech Revolution")
agtech_data = pd.DataFrame({
    'Company': ['CropBiome AI', 'Agri-Tech Centre (Teagasc)', 'ProvEye', 'Micron Agritech'],
    'AI Usage (%)': [82, 65, 70, 60],
    'Blockchain Integration (%)': [60, 48, 40, 35]
})
fig2 = px.scatter(agtech_data, x='AI Usage (%)', y='Blockchain Integration (%)', text='Company',
                 size='AI Usage (%)', title='AI and Blockchain in AgTech Supply Chains - Ireland')
fig2.update_traces(textposition='top center', hovertemplate=crosshair_template)
st.plotly_chart(fig2, use_container_width=True)
st.info("Irish AgTech startups and institutions are leveraging AI and blockchain to drive innovation across the supply chain, with CropBiome AI leading adoption.")

# Theme 3: Talent & Human Capital
st.header("3. Talent & Human Capital")
talent_data = pd.DataFrame({
    'Initiative': ['AgCreds (UCC)', 'Young Farmers Program (Macra na Feirme)', 'AgriAware Schools', 'Teagasc Traineeships'],
    'Youth Programs': [10, 14, 18, 22],
    'Awareness Campaigns': [12, 18, 25, 20]
})
fig3 = px.bar(talent_data, x='Initiative', y=['Youth Programs', 'Awareness Campaigns'],
              title='Human Capital Development in Irish Agriculture', barmode='group')
fig3.update_traces(hovertemplate=crosshair_template)
st.plotly_chart(fig3, use_container_width=True)
st.info("Irish institutions are heavily investing in attracting and training the next generation of agri professionals through practical and academic channels.")

# Theme 4: Climate Resilience
st.header("4. Climate Resilience")
resilience_data = pd.DataFrame({
    'Strategy': ['Peatland Restoration', 'Low-emission slurry spreading', 'Ag-climate PPPs', 'Hedgerow Biodiversity'],
    'Adoption Rate (%)': [70, 80, 62, 68]
})
fig4 = px.pie(resilience_data, values='Adoption Rate (%)', names='Strategy',
              title='Adoption of Climate Resilient Strategies in Ireland')
fig4.update_traces(hovertemplate=crosshair_template)
st.plotly_chart(fig4, use_container_width=True)
st.info("Ireland’s environmental strategies emphasize biodiversity and emissions reduction, with strong public-private collaborations to scale resilience.")

# Theme 5: Food Industry Innovation
st.header("5. Food Industry Innovation")
food_inno_data = pd.DataFrame({
    'Trend': ['Functional Foods (GLP-1)', 'Clean Labels', 'Transparency Tech', 'Irish Regenerative Labels', 'Plant-based R&D'],
    'Impact Score (0-100)': [79, 84, 91, 76, 80]
})
fig5 = px.bar(food_inno_data, x='Trend', y='Impact Score (0-100)', color='Trend',
              title='Emerging Trends in the Irish Food Industry')
fig5.update_traces(hovertemplate=crosshair_template)
st.plotly_chart(fig5, use_container_width=True)
st.info("Transparency, clean labels, and plant-based innovations are reshaping consumer demands and production methods across Ireland’s food industry.")

# Theme 6: Food Security & Equity
st.header("6. Food Security & Equity")
security_data = pd.DataFrame({
    'Organization': ['Bord Bia', 'FAO + Teagasc', 'Irish Organic Association', 'Local Food Hubs'],
    'Smallholder Reach (thousands)': [850, 1250, 560, 320],
    'Equity Model Score (0-100)': [81, 88, 75, 70]
})
fig6 = px.scatter(security_data, x='Smallholder Reach (thousands)', y='Equity Model Score (0-100)',
                  size='Equity Model Score (0-100)', text='Organization',
                  title='Inclusive Business Models for Food Equity in Ireland')
fig6.update_traces(textposition='top center', hovertemplate=crosshair_template)
st.plotly_chart(fig6, use_container_width=True)
st.info("Inclusive food models ensure smallholder participation, particularly with public-sector initiatives like FAO-Teagasc setting a strong example.")

# Closing Note
#st.markdown("""
##---
### 🇮🇪 As IFAMA President, I thank the speakers and participants for shaping Ireland's agri-food future.
#### 🌍 Welcome to Cork 2026: Where Innovation Meets Tradition!
#""")
