from DefCallOpenAIApI import *

Template="""3
DAWID ALBERT LUKASIK
61 Bridge Street, Kington, Herefordshire,
HR5 3DJ, UNITED KINGDOM
P135501:001564/01/001/002
6430/00 40500B
POST Can we help?
If you have any queries or
require information about
your account please contact
Tollcross Branch
865 Shettleston Road
Glasgow G32 7NS
08457 240024
70566110
Your Current Account Plus Statement
Page 1 of 3
Statement No: 716
Date Description Debits Credits Balance
30 Sep 2020 Balance from previous statements 19617.00
01 Oct SO Scottish Power
DDBT Group Plc
6.50
39.11 19656.89
07 Oct 000887 32.43 19689.32
11 Oct 001596
001599
000884 292.00
23.21
426.05
19846.58
13 Oct 001600
001438
000883
000885
000886
760.00
75.00
32.43
40.71
110.00
440.00
19488.44
14 Oct 000888 171.30 19659.74
22 Oct 001439
001440
444.05
20103.79
26 Oct 000889
000890
60.71
124.63
54.05
19864.40
28 Oct 001442
001441
202.50
20066.90
30 Oct Church of Scotland 48.96 20017.94
Tax Deducted
Gross Interest
0.41
2.47 20020.00
Statement date
05 November 2023
Account Name
Hermione Granger
Sort Code
82-20-00
Account Number
70566110
IBAN
GB91CLYD82643070566110
BIC
CLYDGB21430
Opening Balance
£19617.00
Debits
£1512.89
Credits
£1915.89
Closing Balance
£20020.00
Planned Borrowing Limit
Current £1100
DD = Direct Debit
SO = Standing Order
TB = Telephone Banking
TL = Over the Counter
Payment
EB = Electronic Banking
OD = Overdrawn
Cls = Contactless Debit
Interest rate details can be found on Page 2. Card Transaction
From 2nd October 2020, our returned item Fee is being reduced from £35 to £15.
Customers who incur this feel will be notified of it at the end of each calendar month,
giving them at least 14 days’ notice before the fee is debited from their account. The
reduced fee will be debited from customers’ accounts from 21th November 2020 to onwards.
Clydesdale Bank is a trading name of Clydesdale Bank PLC which is authorised and regulated by the Financial Services
Authority. Credit facilities other than regulated mortgages are not regulated by the Financial Services Authority.
Clydesdale Bank PLC Registered in Scotland No. SC001111. Registered Office: 30 St Vincent Place, Glasgow G1 2HL.
A member of National Australia Bank Group.
"""
Response=call_updatedpromptgpt4preview(Template)

print(f"Test output:{Response}")

