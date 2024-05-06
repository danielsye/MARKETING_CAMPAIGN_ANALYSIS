# import libraries
import pandas as pd

cust = pd.read_excel('/workspaces/MARKETING_CAMPAIGN_ANALYSIS/cust_v2.xlsx')
cust

contact = pd.read_csv('/workspaces/MARKETING_CAMPAIGN_ANALYSIS/contact_v2.csv')
contact

``` python
# Check shape of cust
print(cust.shape)
print(cust.columns)
print(cust.index)
```

# Check shape of contact
print(contact.shape)
print(contact.columns)
print(contact.index)