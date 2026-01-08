# Trade-Based Money Laundering: Detecting Anomalies in Dual-Use Agricultural Exports
**Author:** Cristian Morales | **Date:** January 8, 2026
**Field:** Financial Crime & Intelligence Analysis

## 1. Abstract
While financial institutions scrutinize swift transfers, the physical movement of goods remains a blind spot in anti-money laundering (AML) frameworks. This research note analyzes **Trade-Based Money Laundering (TBML)** within the agricultural machinery sector. By applying statistical outlier detection to customs data, we identify systematic over- and under-invoicing used to move illicit capital across borders.

## 2. The Mechanism: Value Transfer
TBML does not move cash; it moves *value*. 
* **To move money OUT of a country:** An importer pays \$150,000 for a tractor worth \$50,000. The extra \$100,000 is "clean" money transferred to the exporter (the criminal associate).
* **To move money IN:** An exporter ships a \$50,000 tractor but invoices it at \$5,000. The importer receives \$45,000 of "free" asset value.

## 3. Methodology
We analyzed a dataset of 200 export transactions for **HS Code 8701** (Tractors) between Port of Manzanillo (Mexico) and Rotterdam. We applied a **Unit Price Analysis** method, calculating the median market price and flagging transactions deviating by >2 standard deviations ($\sigma$).

## 4. Analysis: The Red Dots
Our scatter plot reveals a distinct "barbell" distribution. While 90% of transactions cluster around the Fair Market Value (FMV) of \$50,000, distinct clusters appear at the extremes.

[IMAGE: tbml_scatter_analysis.png]

**Figure 1:** Unit Price Scatter Plot. The blue dots represent legitimate commerce falling within the standard price band. The red dots represent "high-risk" invoices. The clustering of these anomalies suggests automated invoicing fraud rather than clerical error.

## 5. Risk Implications: Dual-Use
Beyond financial crime, these anomalies pose a biosecurity risk. Criminal networks often use agricultural supply chains to traffic "Dual-Use" precursors (chemicals that can be used for both fertilizer and explosives/narcotics). If the invoice is fraudulent, the cargo manifest is likely fraudulent as well.

## 6. Conclusion
Customs agencies must move beyond random physical inspections to algorithmic invoice auditing. Integrating real-time pricing APIs into customs software could flag these value anomalies before the goods clear the port.

## 7. References
1.  Financial Action Task Force (FATF). (2020). *Trade-Based Money Laundering: Trends and Developments.*
2.  Zdanowicz, J. S. (2009). "Trade-based money laundering and terrorist financing." *Review of Law & Economics*.
