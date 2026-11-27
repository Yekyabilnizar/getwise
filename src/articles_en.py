"""English versions of the GetWise guides. Keys are the Indonesian slugs."""
from articles import _efektif
from charts import C, E, G, M, bars, figure, lines


def mn(v):
    return ("Rp" + f"{v/1e6:.1f}".replace(".0", "") + "M") if v else "0"


def k(v):
    return f"Rp{round(v/1000):,}K" if v else "0"


def full(v):
    return f"Rp{round(v):,}"


MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
TIP = lambda t: f'<div class="note info"><b>Tip:</b> {t}</div>'

_u = 6e6 / 173
_rates = [3, 4, 5, 6, 7, 8, 9, 10]
_eff = [_efektif(24e6, (24e6 + 24e6 * r / 100 * 3) / 36, 36) * 100 for r in _rates]
CHARTS_EN = {
    "CH_PPH": figure(bars(MON, [("PPh 21", E, [261350] * 3 + [1840860] + [261350] * 7 + [322840])], k, "Monthly PPh 21 withholding", values_on_top=k),
                     "Example: Rp10 million salary, TK/0 status, Rp10 million bonus in April, all BPJS programs. The deduction jumps in the bonus month and is reconciled in December. Annual total Rp4,777,200."),
    "CH_GAJI": figure(bars(["Gross salary", "BPJS", "PPh 21", "Take-home"], [("", E, [10e6, 400000, 261350, 9338650])], mn, "From gross to net salary", values_on_top=full),
                      "Rp10 million salary (TK/0, all BPJS programs): Rp400,000 BPJS and Rp261,350 PPh 21 are deducted, leaving Rp9,338,650 a month."),
    "CH_BPJS": figure(bars(["Health", "JHT", "JP", "JKK", "JKM"], [("Employer", E, [320000, 296000, 160000, 19200, 24000]), ("Employee", G, [80000, 160000, 80000, 0, 0])], k,
                           "BPJS contributions by program"),
                      "Monthly contributions for a Rp8 million wage. The employer pays the larger share; the employee pays only Health 1%, JHT 2%, and JP 1%."),
    "CH_THR": figure(bars([str(i) for i in range(1, 13)], [("THR", G, [6e6 * i / 12 for i in range(1, 13)])], mn, "THR by length of service", values_on_top=mn),
                     "THR for a Rp6 million wage by months of service. From 12 months, THR is a full month's wages."),
    "CH_KPR": figure(bars([str(i) for i in range(1, 16)], [("Monthly installment", E, [3671968] * 3 + [5114414] * 12)], mn, "Mortgage installment by year", values_on_top=mn),
                     "Rp480 million KPR (Rp600 million house, 20% down), 15-year term, 4.5% fixed for 3 years then 11% floating. The installment rises about 39% in year 4."),
    "CH_FLAT": figure(bars([f"{r}%" for r in _rates], [("Flat rate", G, _rates), ("Equivalent effective rate", E, _eff)], lambda v: f"{v:.0f}%", "Flat vs. effective rate"),
                      "For a 36-month term, the effective rate is about 1.8 times the flat rate. A 6% flat rate equals roughly 11% effective per year."),
    "CH_DEPO": figure(bars(["3%", "4%", "5%", "6%"], [("Gross interest", M, [3e6, 4e6, 5e6, 6e6]), ("Net interest (after 20% tax)", E, [2.4e6, 3.2e6, 4e6, 4.8e6])], mn,
                           "One-year deposit interest"),
                      "One-year interest on a Rp100 million deposit at several rates. The 20% tax takes one fifth of the return."),
    "CH_INV": figure(lines([str(i) for i in range(1, 21)], [("10% return", G, [12.5, 26.3, 41.5, 58.2, 76.6, 96.8, 119, 143.4, 170.3, 199.9, 232.4, 268.2, 307.5, 350.8, 398.4, 450.8, 508.5, 571.8, 641.6, 718.3]),
                                                           ("6% return", E, [12.3, 25.4, 39.2, 53.9, 69.5, 86, 103.5, 122, 141.6, 162.5, 184.5, 207.9, 232.8, 259, 286.9, 316.5, 347.8, 381, 416.1, 453.4]),
                                                           ("Savings only (0%)", M, [12 * i for i in range(1, 21)])],
                           lambda v: f"{v:.0f}M", "Growth of Rp1 million a month", step=2),
                     "Investing Rp1 million a month for 20 years: total contributions Rp240 million. At 6% a year it grows to about Rp453 million; at 10%, about Rp718 million."),
    "CH_LEMBUR": figure(bars(["1 hour", "2 hours", "3 hours", "4 hours"], [("Overtime pay", E, [_u * 1.5 + _u * 2 * (h - 1) for h in range(1, 5)])], k, "Overtime pay on a working day", values_on_top=full),
                        "Overtime pay on a working day for a Rp6 million monthly wage (hourly wage = Rp6,000,000 ÷ 173 ≈ Rp34,682). The first hour is paid at 1.5×, later hours at 2×."),
    "CH_ANGGARAN": figure(bars(["Needs (50%)", "Wants (30%)", "Savings & investing (20%)"], [("", E, [4e6, 2.4e6, 1.6e6])], mn, "50/30/20 budget", values_on_top=mn),
                          "Example split of an Rp8 million monthly take-home pay using the 50/30/20 rule."),
    "CH_PINJAM": figure(bars(["Online loan (0.2%/day)", "Credit card (1.75%/month)", "Bank personal loan (e.g. 12%/yr)"], [("Cost", C, [300000, 87500, 50000])], k,
                             "Cost of borrowing Rp5 million for 30 days", values_on_top=full),
                        "Illustrative interest cost of borrowing Rp5 million for 30 days. Rates are examples only; actual rates vary by product and over time."),
    "CH_TAKEOVER": figure(bars(["11% rate", "8% rate"], [("Monthly installment", E, [5014221, 4329810])], mn, "Installment before and after refinancing", values_on_top=full),
                          "Remaining principal Rp400 million with 12 years left. Dropping from 11% to 8% saves about Rp684,000 a month, or about Rp98.6 million over the remaining term, before refinancing costs."),
    "CH_DARURAT": figure(bars(["Single", "Married", "Married + children", "Self-employed / freelancer"], [("Emergency fund", G, [15e6, 30e6, 45e6, 60e6])], mn, "Emergency fund target", values_on_top=mn),
                         "Example emergency fund targets for Rp5 million monthly expenses: 3, 6, 9, and 12 times monthly spending."),
}

ART_EN = {}


def A(sid, **kw):
    ART_EN[sid] = kw


A("apa-itu-pph-21-ter", slug="what-is-pph-21-and-ter",
  title="What Is PPh 21 and the TER Method? A Complete Guide for Employees in Indonesia",
  h1="What Is PPh 21 and the TER Method?",
  desc="What Indonesian income tax on salary (PPh 21) is, how the average effective rate (TER) works, why December's deduction is different, and tips to avoid payslip surprises.",
  lead="PPh 21 is the tax deducted from your salary every month. Since 2024 it has been withheld with the TER method. Here is a simple explanation.",
  body=[
      ("What is PPh 21?", """<p><b>PPh Article 21</b> is the income tax on salaries, wages, fees, allowances, and other payments individuals receive for work in Indonesia. Employees don't pay it themselves: the <b>employer withholds</b> the tax from salary, pays it to the state, and reports it. At year end the company issues a withholding slip (form 1721-A1) that you use for your annual tax return (SPT).</p>
<p>The amount differs from person to person. Two things matter most: <b>how much you earn</b> and <b>your family status</b> (PTKP). The higher the income, the higher the bracket; the more dependants, the larger the tax-free portion.</p>"""),
      ("PTKP: the non-taxable portion", """<p><b>PTKP (Penghasilan Tidak Kena Pajak)</b> is the annual income that is exempt from tax. It is Rp54 million for yourself, plus Rp4.5 million if married, and Rp4.5 million for each dependant (children or fully supported relatives), up to three.</p>
<ul><li><b>TK/0</b> (single, no dependants): Rp54,000,000</li><li><b>K/0</b> (married, no children): Rp58,500,000</li><li><b>K/2</b> (married, two children): Rp67,500,000</li><li><b>K/3</b> (married, three children): Rp72,000,000</li></ul>
<p>So a single employee with annual net income below Rp54 million owes no PPh 21 at all.</p>"""),
      ("How the TER method works", """<p>Before 2024, employers calculated the annual tax and divided it by month, which was complicated. Through PP 58/2023 and PMK 168/2023, the government introduced the <b>average effective rate (TER)</b> to simplify it:</p>
<ol><li><b>January to November</b>: tax = that month's gross income × TER rate. The rate comes from table A (TK/0, TK/1, K/0), B (TK/2, TK/3, K/1, K/2), or C (K/3), based on monthly gross income.</li>
<li><b>December</b>: the annual tax is recalculated with the progressive Article 17 rates (5%, 15%, 25%, 30%, 35%), minus what has already been withheld. The remainder is December's deduction.</li></ol>
<p>Because TER looks at one month at a time, the deduction can spike in the month you receive a bonus or THR. The spike is not extra tax; everything is reconciled in December.</p>
[[CH_PPH]]"""),
      ("Components people forget", """<p>Gross income for TER is more than the base salary. <b>BPJS Health, JKK, and JKM premiums paid by the employer</b> are counted as income even though you don't receive them in cash. On the other hand, your <b>JHT 2% and JP 1%</b> contributions are deducted in the December calculation, along with the <b>job expense deduction</b> of 5% (maximum Rp6 million a year).</p>
<p>That is why the tax on your payslip often looks slightly higher than a calculation based on base salary alone.</p>"""),
      ("Tips to avoid surprises", "<ul>"
       "<li><b>Check your PTKP status with HR.</b> If you are married or have children but the system still says TK/0, too much tax is withheld. The status used is the one at the start of the tax year.</li>"
       "<li><b>Plan for bonus and THR months.</b> The deduction can be several times a normal month. Budget from net THR, not gross.</li>"
       "<li><b>Don't panic at December's payslip.</b> It may be higher (under-withheld) or lower, even a refund (over-withheld).</li>"
       "<li><b>Keep your 1721-A1 slip.</b> You need it to file your annual tax return by 31 March of the following year.</li>"
       "<li><b>Changed jobs mid-year?</b> Get the withholding slip from your old employer and give it to the new one, or combine them in your return, so the annual tax is calculated correctly.</li></ul>"
       + TIP("use the PPh 21 calculator to see the deduction for each month, including bonus months and December, before your payslip arrives.")),
  ],
  faq=[("Is every employee subject to PPh 21?", "Only if annual net income exceeds PTKP. The employer still has to calculate and report it."),
       ("Does TER increase the tax burden?", "No. TER only changes monthly withholding. Total annual tax is still set by the Article 17 rates in the last tax period.")])

A("cara-membaca-slip-gaji", slug="how-to-read-your-payslip",
  title="How to Read an Indonesian Payslip: Gross Pay, Deductions, and Take-Home Pay",
  h1="How to Read Your Payslip and Calculate Take-Home Pay",
  desc="Understand an Indonesian payslip: base salary, fixed and variable allowances, BPJS and PPh 21 deductions, plus tips for managing your take-home pay.",
  lead="The amount in your bank account is almost always smaller than the salary in your contract. Learn the parts of a payslip so you know where the difference goes.",
  body=[
      ("Gross vs. net salary", """<p><b>Gross salary</b> is total pay before deductions: base salary plus all allowances. <b>Net salary</b> or <b>take-home pay (THP)</b> is what you actually receive after mandatory contributions and tax. When negotiating or comparing job offers, make sure you know whether the number discussed is gross or net.</p>
[[CH_GAJI]]"""),
      ("Income components on a payslip", """<ul><li><b>Base salary</b>: the core pay for the position and seniority.</li>
<li><b>Fixed allowances</b>: paid regularly in the same amount each month regardless of attendance, such as position or family allowances. Base salary + fixed allowances are called <b>wages (upah)</b> and are the basis for BPJS, THR, and severance.</li>
<li><b>Variable allowances</b>: depend on attendance or performance, such as daily meal and transport allowances, overtime, and incentives.</li>
<li><b>Irregular income</b>: bonuses, THR, and back pay from raises.</li></ul>
<p>Under the wage rules, base salary should be at least 75% of base salary plus fixed allowances.</p>"""),
      ("Deductions", """<ul><li><b>BPJS Health 1%</b> of wages (Rp12 million cap).</li>
<li><b>JHT 2%</b> of wages, your own old-age savings at BPJS Employment.</li>
<li><b>JP 1%</b> of wages (Rp11,086,300 cap from March 2026), for a monthly pension.</li>
<li><b>PPh 21</b> with the TER method.</li>
<li>Other company-specific deductions: cooperative dues, staff loans, union fees, or late penalties.</li></ul>
<p>JHT and JP are not really &ldquo;lost&rdquo;. Both come back to you as your JHT balance and pension benefits.</p>"""),
      ("Tips for managing take-home pay", "<ul>"
       "<li><b>Budget from your average THP</b>, not the contract salary. December's tax can differ from other months.</li>"
       "<li><b>Use the 50/30/20 rule</b> as a starting point: 50% needs, 30% wants, 20% savings and investing.</li>"
       "<li><b>Pay yourself first</b>: set an automatic transfer to savings or investments on payday.</li>"
       "<li><b>Build an emergency fund</b> of 3–6 months of expenses before investing in riskier assets.</li>"
       "<li><b>Check your payslip every month.</b> Wrong PTKP status, under-reported BPJS wages, or unpaid overtime are easier to fix early.</li>"
       "<li><b>Check your JHT balance</b> in the official BPJS Employment app to make sure contributions are actually paid.</li></ul>"
       + TIP("when comparing two job offers, calculate the take-home pay of each with the take-home pay calculator; variable allowances and benefits can make a big difference.")),
  ],
  faq=[("Why is December's net pay different?", "Because December's PPh 21 is recalculated for the whole year. It can be higher or lower than other months."),
       ("Is meal allowance part of wages for BPJS?", "Not if it is paid per attendance day. Daily meal allowance is a variable allowance, but it still counts as income for tax.")])

A("aturan-thr-dan-tips-mengelolanya", slug="thr-rules-and-tips",
  title="THR Rules in Indonesia: Who Is Entitled, How to Calculate, and How to Manage It",
  h1="THR Rules: Entitlement, Calculation, and Tips",
  desc="Guide to THR (religious holiday allowance) in Indonesia: legal basis, who is entitled, the pro-rata formula, payment deadline, tax on THR, and tips for using it wisely.",
  lead="The Religious Holiday Allowance (THR) is an employee right that employers must pay before a religious holiday. Here are the rules and how to calculate it.",
  body=[
      ("What THR is and the legal basis", """<p><b>THR (Tunjangan Hari Raya Keagamaan)</b> is non-wage income employers must pay before a religious holiday: Eid al-Fitr, Christmas, Nyepi, Vesak, or Chinese New Year according to the employee's religion (or as agreed). The main rule is <b>Minister of Manpower Regulation 6/2016</b>, reinforced by government wage regulations.</p>
<p>THR must be paid <b>no later than 7 days before the holiday</b> and may not be paid in installments unless the government issues special provisions. The Ministry of Manpower usually issues a circular every year reaffirming this obligation.</p>"""),
      ("Who is entitled?", """<ul><li>Employees with at least <b>1 month of continuous service</b>.</li>
<li>Both permanent (PKWTT) and fixed-term (PKWT) employees.</li>
<li>Daily casual workers too, based on average wages.</li>
<li>Permanent employees laid off within 30 days before the holiday are still entitled.</li></ul>"""),
      ("How to calculate THR", """<p>THR is based on <b>one month's wages</b>: base salary plus fixed allowances.</p>
<div class="formula">Service ≥ 12 months : THR = 1 × wages
Service 1–12 months : THR = (months of service ÷ 12) × wages</div>
<p>Example: wages Rp6,000,000 and 8 months of service, THR = 8/12 × Rp6,000,000 = Rp4,000,000. For daily casual workers with 12 months or more, one month's wages is the average of the last 12 months; with less than 12 months, the monthly average over the period worked.</p>
[[CH_THR]]"""),
      ("THR and tax", """<p>THR is income subject to PPh 21. With TER, tax for the THR month is calculated on salary plus THR, so the rate moves to a higher bracket and the deduction spikes. In December, all income for the year is recalculated with Article 17 rates, so total annual tax does not increase just because of this withholding method.</p>"""),
      ("Tips for managing THR", "<ul>"
       "<li><b>Work out net THR first</b>, after tax, before planning spending.</li>"
       "<li><b>Split it into buckets</b>: holiday needs, zakat or charity, travel home, and savings. Decide the percentages before the money arrives.</li>"
       "<li><b>Pay off high-interest debt</b> such as credit cards or paylater before consumer spending.</li>"
       "<li><b>Keep some for after the holiday.</b> Spending often balloons while the next salary is weeks away.</li>"
       "<li><b>Beware of sales.</b> Make a shopping list and a budget so THR isn't spent on unplanned items.</li></ul>"
       + TIP("if THR is not paid or is late, employees can report it to the Ministry of Manpower's THR complaint post or the local manpower office. Employers who pay late are fined 5% of total THR, and the fine does not remove the obligation to pay.")),
  ],
  faq=[("Can THR be more than one month's wages?", "Yes, if set out in the employment agreement, company regulations, collective agreement, or established practice."),
       ("Are employees who resign entitled to THR?", "For permanent employees, yes if employment ends within 30 days before the holiday. Otherwise, generally not.")])

A("mengenal-bpjs-kesehatan-dan-ketenagakerjaan", slug="bpjs-health-and-employment-explained",
  title="BPJS Health and BPJS Employment Explained: Programs, Benefits, and Contributions",
  h1="BPJS Health and BPJS Employment Explained",
  desc="A complete guide to BPJS programs for employees in Indonesia: Health, JHT, JP, JKK, JKM, and JKP, contribution rates, benefits, and tips to make sure you get your rights.",
  lead="Every employee in Indonesia must be enrolled in BPJS. Contributions are deducted from salary, but many people don't know what benefits they actually get.",
  body=[
      ("Two agencies, six programs", """<p>Social security in Indonesia is run by two agencies. <b>BPJS Kesehatan</b> runs the National Health Insurance (JKN). <b>BPJS Ketenagakerjaan</b> runs five programs: Old-Age Savings (JHT), Pension (JP), Work Accident (JKK), Death (JKM), and Job Loss (JKP).</p>
[[CH_BPJS]]"""),
      ("BPJS Health", """<p>Provides healthcare from community health centers or clinics (primary care) up to hospitals through a referral system. Contributions for salaried workers are <b>5% of wages</b>: 4% paid by the employer and 1% deducted from salary, with a Rp12 million wage cap. This covers the member, spouse, and up to three children.</p>
<p>The government is also gradually introducing <b>Standard Inpatient Class (KRIS)</b> to standardize inpatient rooms. Follow official BPJS Health announcements for the latest developments.</p>"""),
      ("BPJS Employment programs", """<ul><li><b>JHT</b>: savings funded jointly (3.7% employer, 2% employee) and invested by BPJS. The balance can be withdrawn when you stop working, retire, become permanently disabled, or die; part of it can be claimed early for home ownership or other purposes after 10 years of membership.</li>
<li><b>JP</b>: a monthly pension after reaching retirement age, with at least 15 years of contributions. Contribution 3% (2% employer, 1% employee) with a wage cap that rises every year.</li>
<li><b>JKK</b>: covers unlimited treatment costs as medically required for work accidents or occupational diseases, including accidents commuting to and from work. 0.24%–1.74% paid by the employer.</li>
<li><b>JKM</b>: benefits for heirs if the member dies from causes other than a work accident, including scholarships for children under the rules. 0.3% paid by the employer.</li>
<li><b>JKP</b>: for those who lose their job, cash benefits for several months, labor-market information, and job training. No additional contribution.</li></ul>"""),
      ("Tips to make sure you get your rights", "<ul>"
       "<li><b>Install the official apps</b> (Mobile JKN and JMO) to check membership status and JHT balance. Make sure contributions are recorded every month.</li>"
       "<li><b>Check the reported wage.</b> If the employer reports a lower wage than you actually earn, your JHT balance and pension will be smaller too.</li>"
       "<li><b>Register family members</b> (spouse and children) with BPJS Health so they are covered at no extra cost.</li>"
       "<li><b>Follow the referral path</b>: start at primary care unless it is an emergency.</li>"
       "<li><b>Report work accidents</b> to your employer quickly so the JKK claim can be processed.</li>"
       "<li><b>Don't rush to withdraw JHT</b> unless you need it. The balance keeps growing for retirement.</li></ul>"
       + TIP("an employer that deducts contributions from salary but does not pay them in is breaking the rules. Report it to BPJS or the local manpower office.")),
  ],
  faq=[("Do BPJS contributions reduce tax?", "The employee's JHT and JP contributions reduce taxable income. The employee's BPJS Health contribution does not."),
       ("Can I have BPJS Health and private insurance?", "Yes. Some private insurers offer coordination of benefits (COB) with BPJS Health.")])

A("panduan-kpr-rumah-pertama", slug="first-home-mortgage-kpr-guide",
  title="First-Home Mortgage (KPR) Guide: Requirements, Fixed vs. Floating Rates, and Approval Tips",
  h1="Mortgage (KPR) Guide for First-Time Buyers",
  desc="What a KPR is, how fixed and floating rates work, application requirements, costs to prepare, and tips to get approved while keeping installments safe.",
  lead="A KPR (home ownership loan) lets you buy a house and pay over decades. Understand how it works before signing.",
  body=[
      ("What is a KPR?", """<p>A <b>KPR</b> is a bank loan to buy a house, with the house itself as collateral. You pay a down payment, the bank finances the rest, and you repay monthly over the agreed term, usually 5 to 25 years. While the loan is running, the bank holds the title certificate and returns it once the loan is paid off.</p>
<p>Besides conventional KPR, there is <b>sharia KPR</b> with contracts such as murabahah (sale with a fixed margin), and <b>subsidized KPR</b> (FLPP) for low-income households with a low fixed rate for the whole term.</p>"""),
      ("Fixed and floating rates", """<p>Conventional KPRs usually start with a <b>fixed rate</b> for, say, 3–5 years, then switch to a <b>floating rate</b> that follows market rates. Installments use the annuity method: the amount stays the same while the rate doesn't change and is recalculated when the floating rate kicks in.</p>
[[CH_KPR]]
<p>This is the biggest risk of a KPR: installments can rise significantly after the promotional period. Always simulate installments with a realistic floating rate before choosing a house.</p>"""),
      ("General requirements", """<ul><li>Indonesian citizen, at least 21 years old or married, and not above the bank's age limit at the end of the loan (usually 55–65).</li>
<li>Regular income with at least 1–2 years of employment, or an established business for the self-employed.</li>
<li>Documents: ID card (KTP), family card (KK), tax ID (NPWP), payslips or financial statements, recent bank statements, and property documents.</li>
<li>A clean credit history in <b>SLIK OJK</b>. Credit card arrears or online loan defaults can get an application rejected.</li></ul>"""),
      ("Costs beyond the down payment", """<p>Many first-time buyers only prepare the down payment. There are other upfront costs: bank provision and admin fees, appraisal, notary and deeds (AJB, APHT), life and fire insurance, and <b>BPHTB</b> (buyer's tax) unless covered by the developer or a government program. Together these can reach several percent of the house price, so ask for the breakdown early.</p>"""),
      ("Tips for approval and safe installments", "<ul>"
       "<li><b>Keep installments under 30–35% of income</b>, including other existing loans.</li>"
       "<li><b>Clean up your credit history</b> a few months before applying: clear arrears and reduce unused credit card limits.</li>"
       "<li><b>Increase the down payment</b> if possible. A smaller principal means much less total interest.</li>"
       "<li><b>Compare several banks</b>, not just promotional rates, but also historical floating rates, prepayment penalties, and fees.</li>"
       "<li><b>Keep a reserve</b> of at least 6 installments in case your income is disrupted.</li>"
       "<li><b>Consider partial prepayment</b> or refinancing when floating rates are high.</li></ul>"
       + TIP("run the mortgage calculator with several floating-rate scenarios, such as 10%, 12%, and 13%, to make sure installments stay affordable.")),
  ],
  faq=[("KPR now or save first?", "It depends on how fast house prices rise where you want to buy, how stable your income is, and whether your emergency fund is ready. A KPR gets you a home sooner, at the cost of interest."),
       ("What is a KPR take over?", "Moving your remaining KPR to another bank with a lower rate. Compare the costs (penalty, provision, notary) with the interest savings.")])

A("bunga-flat-vs-efektif-kredit-kendaraan", slug="flat-vs-effective-interest-vehicle-loans",
  title="Flat vs. Effective Interest: A Guide to Car and Motorcycle Loans in Indonesia",
  h1="Flat vs. Effective Interest on Vehicle Loans",
  desc="The difference between flat and effective interest, why flat rates look cheap, hidden costs of vehicle loans, and tips for choosing a financing company.",
  lead="Car and motorcycle loan brochures often show an interest rate that looks small. Learn how to read it so you know the real cost.",
  body=[
      ("What is a flat rate?", """<p>A <b>flat rate</b> is charged on the original principal for the whole term, even though the outstanding debt falls every month. The installment is easy to calculate: (principal + principal × rate × years) ÷ number of months. Financing companies (leasing) commonly use this method for vehicle loans.</p>
<p>An <b>effective rate</b> is charged on the remaining principal. Interest is high at first and shrinks over time. This is the method used for mortgages and most bank loans.</p>"""),
      ("Why flat rates look cheaper", """<p>With a flat rate you pay interest on the full original principal to the end, while the average outstanding balance over the term is only about half. As a result, a flat rate is equivalent to an effective rate almost <b>twice as high</b>.</p>
[[CH_FLAT]]
<p>So when comparing a leasing offer with a bank loan or personal loan, convert everything to the effective rate first.</p>"""),
      ("Costs beyond the installment", """<ul><li><b>Down payment</b> and the first installment, often paid upfront.</li>
<li><b>Admin and provision fees.</b></li><li><b>Vehicle insurance</b>, comprehensive or total loss only, often included in the installment.</li>
<li><b>Fiduciary fee</b> to register the vehicle as collateral.</li><li><b>Daily late fines</b> and <b>early-repayment penalties</b>.</li></ul>
<p>Ask for the <b>total amount payable</b> (down payment + all installments + other fees) in writing, then compare it with the cash price.</p>"""),
      ("Tips for choosing a vehicle loan", "<ul>"
       "<li><b>Choose a financing company registered and supervised by OJK.</b></li>"
       "<li><b>Large down payment, short term.</b> This combination saves the most interest.</li>"
       "<li><b>Keep vehicle installments</b> around 10–15% of income so they don't squeeze essentials and savings.</li>"
       "<li><b>Count the cost of ownership</b>: fuel, annual tax, servicing, parking, and insurance after the loan ends.</li>"
       "<li><b>Read the agreement before signing</b>, especially fines, repossession, and early repayment.</li>"
       "<li><b>Don't transfer the loan informally.</b> Passing it on without the lender's approval carries legal risk.</li></ul>"
       + TIP("use the vehicle loan calculator to see the effective rate behind a flat-rate offer, then compare it with a bank loan.")),
  ],
  faq=[("Can I pay off the loan early?", "Usually yes, but check the penalty and how remaining interest is calculated. With flat interest, the savings are often smaller than expected."),
       ("Can the lender repossess the vehicle unilaterally?", "Repossession must follow the law and the fiduciary agreement. If there is a dispute, consult OJK or a dispute resolution body.")])

A("panduan-deposito-untuk-pemula", slug="time-deposits-for-beginners",
  title="Time Deposits for Beginners: How They Work, Tax, LPS Guarantee, and Tips",
  h1="A Beginner's Guide to Time Deposits",
  desc="What a time deposit (deposito) is, its types, how interest and the 20% tax are calculated, LPS guarantee conditions, comparison with savings, and tips for choosing a deposit.",
  lead="Time deposits are one of the simplest and safest ways to grow money. Learn how they work to get the most out of them.",
  body=[
      ("What is a time deposit?", """<p>A <b>time deposit (deposito berjangka)</b> is a bank deposit that can only be withdrawn after a fixed term, such as 1, 3, 6, 12, or 24 months. In return for &ldquo;locking&rdquo; the money, the bank pays higher interest than a regular savings account, and the rate is fixed from the start.</p>
<p>Besides conventional deposits, there are <b>sharia deposits</b> with profit sharing (nisbah), and deposits that can be opened entirely online through banking apps with a smaller minimum.</p>"""),
      ("Interest and tax", """<p>Deposit interest is subject to a <b>20% final tax</b> withheld by the bank. Interest is not taxed if your total deposits at that bank do not exceed Rp7.5 million.</p>
[[CH_DEPO]]
<p>At maturity you can choose <b>ARO</b> (automatic rollover), with interest added to principal so it compounds, or have interest paid to your savings account.</p>"""),
      ("The LPS guarantee", """<p>Deposits at banks participating in the <b>Indonesia Deposit Insurance Corporation (LPS)</b> are guaranteed up to <b>Rp2 billion per customer per bank</b>. To be covered, three main conditions apply: the deposit is recorded in the bank's books, the interest you receive <b>does not exceed the LPS guaranteed rate</b>, and you did not cause the bank's failure.</p>
<p>The second condition is often overlooked. If a bank offers far more than the LPS guaranteed rate, your deposit may not be covered. Check the latest guaranteed rate on the official LPS website, as it is reviewed periodically.</p>"""),
      ("Tips for choosing and using deposits", "<ul>"
       "<li><b>Use deposits for clear goals</b> with a fixed timeline, such as a house down payment in two years or school fees next year.</li>"
       "<li><b>Don't keep your whole emergency fund in deposits.</b> Early withdrawal can be penalized.</li>"
       "<li><b>Split into several deposits</b> with different maturity dates (laddering) so part of the money is always available.</li>"
       "<li><b>Compare net returns</b> with alternatives such as money market funds or retail government bonds (SBN), which are taxed differently.</li>"
       "<li><b>Watch inflation.</b> Net interest below inflation still erodes your purchasing power.</li>"
       "<li><b>Make sure the bank is registered with OJK and participates in LPS</b>, especially digital banks or rural banks (BPR) offering high rates.</li></ul>"
       + TIP("calculate net interest after tax with the deposit calculator, then compare it with the net return of other instruments before deciding.")),
  ],
  faq=[("What is the minimum to open a deposit?", "It varies by bank. Branch deposits usually start at a few million rupiah, while online deposits at digital banks can be much smaller."),
       ("Is a deposit an investment?", "A deposit is a very low-risk savings product. It is good for preserving value in the short term, but returns are limited.")])

A("bunga-majemuk-dan-investasi-rutin", slug="compound-interest-and-regular-investing",
  title="Compound Interest and Regular Investing: Making Money Work for You",
  h1="Compound Interest and Regular Investing for Beginners",
  desc="What compound interest is, why time is the key, investment options in Indonesia, and tips to start investing regularly every month.",
  lead="Compound interest lets your returns earn returns. The earlier and more regularly you start, the bigger the effect.",
  body=[
      ("What is compound interest?", """<p><b>Compound interest</b> means returns are not withdrawn but added to the capital, so the next period earns on them too. The result grows like a snowball: slowly at first, then faster over time.</p>
[[CH_INV]]
<p>The chart shows two important things. First, <b>time</b> is the biggest factor: the gap between saving and investing widens sharply after 10 years. Second, a difference of a few percentage points a year creates a gap of hundreds of millions of rupiah in the long run.</p>"""),
      ("Regular investing (dollar cost averaging)", """<p>Investing the same amount every month is called <b>regular investing</b> or dollar cost averaging. You don't need to time the market: when prices fall, the same amount buys more units; when prices rise, your holdings gain value. The habit also builds discipline, especially if automated on payday.</p>"""),
      ("Investment options", """<ul><li><b>Money market funds</b>: low risk, suitable for emergency funds and goals under 1 year.</li>
<li><b>Retail government bonds (SBN)</b> (ORI, SBR, Retail Sukuk, Savings Sukuk): state-guaranteed with fixed or floating coupons. Coupons are subject to a 10% final tax.</li>
<li><b>Fixed income funds</b>: invested in bonds, suitable for 1–3 years.</li>
<li><b>Equity funds and stocks</b>: highest potential long-term return, but values can swing sharply. Suitable for goals beyond 5 years.</li>
<li><b>Gold</b>: often used as a hedge, with no regular income.</li></ul>
<p>Make sure products and apps are <b>registered with and supervised by OJK</b>. Be wary of offers with guaranteed high returns; that is a hallmark of investment scams.</p>"""),
      ("Tips for starting regular investing", "<ul>"
       "<li><b>Build an emergency fund first</b>, at least 3–6 months of expenses, in something easy to withdraw.</li>"
       "<li><b>Set goals and timelines</b>, such as an education fund in 10 years or retirement in 25 years. The timeline determines the right instrument.</li>"
       "<li><b>Start small but regularly.</b> Many funds can be started from Rp10,000–Rp100,000.</li>"
       "<li><b>Raise contributions whenever your salary rises.</b> A 5–10% annual increase makes a big difference.</li>"
       "<li><b>Diversify</b>; don't put all your money in one product.</li>"
       "<li><b>Account for inflation.</b> Subtract expected inflation from returns to see the real value.</li>"
       "<li><b>Don't panic when markets fall.</b> For long-term goals, temporary drops are a chance to buy cheaper.</li></ul>"
       + TIP("simulate several return scenarios (pessimistic, moderate, optimistic) in the investment calculator to find the monthly contribution needed to reach your goal.")),
  ],
  faq=[("What return is realistic?", "It depends on the instrument and market conditions. Only savings products and fixed-coupon SBN have guaranteed returns. Use several scenarios."),
       ("Lump sum or regular investing?", "A lump sum can win if markets keep rising, but regular investing is easier to stick to and reduces the risk of buying at a peak.")])

A("cara-lapor-spt-tahunan-karyawan", slug="how-to-file-annual-tax-return-employees",
  title="How Employees File the Annual Tax Return (SPT) in Coretax: Steps, Documents, and Tips",
  h1="How to File Your Annual Tax Return (SPT) as an Employee",
  desc="Guide to filing the individual annual tax return (SPT Tahunan) in Indonesia via Coretax DJP: documents to prepare, filing steps, deadline, penalties, and tips.",
  lead="Even though your employer withholds tax every month, employees must still file an annual tax return. Here are the steps and tips.",
  body=[
      ("Why employees still need to file", """<p>PPh 21 withheld by your employer is a <b>payment</b> of tax. The <b>annual tax return (SPT Tahunan)</b> is your own <b>report</b> to the state on your income, assets, debts, and tax for the year. They are different: tax may be fully paid, but every registered taxpayer (the NIK now serves as the tax ID) still has to report.</p>
<p>Since the 2025 tax year, annual returns are filed through the <b>Coretax DJP</b> system, replacing the old DJP Online and e-Filing.</p>"""),
      ("Documents to prepare", """<ul><li><b>PPh 21 withholding slip (form 1721-A1)</b> from your employer, or A2 for civil servants. If you changed jobs, collect slips from every employer.</li>
<li>An activated <b>Coretax account</b>, with your password and electronic certificate or authorization code for the digital signature.</li>
<li><b>List of assets</b> as of 31 December: savings, deposits, vehicles, property, and investments with their acquisition values.</li>
<li><b>List of debts</b>: remaining mortgage, vehicle loan, credit cards, and other loans.</li>
<li><b>Family data</b> for dependants.</li>
<li>Proof of other income, if any, such as deposit interest (final tax) or side income.</li></ul>"""),
      ("Filing steps in Coretax", """<ol><li>Log in to Coretax DJP with your NIK and password.</li>
<li>Open the <b>Surat Pemberitahuan (SPT)</b> menu and choose <b>Buat Konsep SPT</b> (create draft).</li>
<li>Select <b>PPh Orang Pribadi</b> (individual income tax), annual return, period, and tax year. Choose <b>Normal</b> for a first filing.</li>
<li>Open the draft. The system prefills some data, including income and tax from withholding slips reported by employers.</li>
<li>Review and complete: other income, assets, debts, and dependants.</li>
<li>Check the result. For employees with one employer, it is usually <b>nil</b> because tax was withheld correctly.</li>
<li>Click <b>Bayar dan Lapor</b> (pay and report), then sign digitally. Keep the electronic receipt (BPE).</li></ol>
<p>If the result is <b>underpaid</b>, the system generates a billing code for payment. If <b>overpaid</b>, you can choose a refund or carry it forward.</p>"""),
      ("Deadline and penalties", """<p>Individual annual returns must be filed <b>within 3 months after the end of the tax year</b>, which is 31 March. Late filing incurs an administrative fine of <b>Rp100,000</b>. If an extension or penalty waiver is announced because of system problems, follow official DJP information.</p>"""),
      ("Tips to avoid mistakes", "<ul>"
       "<li><b>Ask for your withholding slip in January.</b> Employers must provide it within a month after the tax year ends.</li>"
       "<li><b>Match the slip with your payslips.</b> Errors in PTKP status or income should be corrected by the employer.</li>"
       "<li><b>Report assets at acquisition value</b>, not current market value.</li>"
       "<li><b>Don't wait until late March.</b> The system gets busy near the deadline.</li>"
       "<li><b>Keep the BPE and all documents</b> for at least five years.</li>"
       "<li>If in doubt, call <b>Kring Pajak 1500200</b> or visit the nearest tax office.</li></ul>"
       + TIP("before filing, double-check your annual tax with the PPh 21 calculator, especially if you received a bonus or changed jobs.")),
  ],
  faq=[("Will my return definitely be nil?", "If you only had one employer and tax was withheld correctly, it is usually nil. With two employers in a year or other income, it may be underpaid."),
       ("Do I have to file if my income is below PTKP?", "If you are registered as a taxpayer, yes. Taxpayers with income below PTKP can apply for non-effective status under the rules.")])

A("cara-menghitung-upah-lembur", slug="how-to-calculate-overtime-pay",
  title="How to Calculate Overtime Pay in Indonesia Under PP 35/2021 (Working Days and Holidays)",
  h1="How to Calculate Overtime Pay in Indonesia",
  desc="The official overtime formula under PP 35/2021: hourly wage of 1/173, overtime rates on working days and holidays, overtime limits, worked examples, and tips to make sure overtime is paid.",
  lead="Overtime is a right with clear rules, including how to calculate the pay. Here is the official formula with examples.",
  body=[
      ("Overtime rules", """<p>Overtime is work beyond normal hours (7 hours a day for a 6-day week, or 8 hours a day for a 5-day week, 40 hours a week in total), or work on weekly rest days and public holidays. The rules are in <b>PP 35/2021</b>, implementing the Job Creation Law.</p>
<ul><li>Overtime requires the employee's <b>instruction and consent</b>, preferably in writing.</li>
<li>Maximum <b>4 hours a day and 18 hours a week</b> (excluding overtime on holidays).</li>
<li>Employees working overtime are entitled to overtime pay, adequate rest, and food and drink of at least 1,400 calories for 4 hours or more.</li></ul>"""),
      ("The overtime formula", """<div class="formula">Hourly wage = 1/173 × monthly wage
(wage = base salary + fixed allowances; if fixed allowances
 exceed 25%, the base is at least 75% of total wages)</div>
<p><b>Overtime on working days:</b> first hour 1.5 × hourly wage; second hour onward 2 × hourly wage.</p>
<p><b>Overtime on rest days or public holidays</b> (6-day week): first 7 hours 2×, 8th hour 3×, 9th to 10th hour 4×. For a 5-day week: first 8 hours 2×, 9th hour 3×, 10th to 11th hour 4×.</p>
[[CH_LEMBUR]]"""),
      ("Example: overtime on a day off", """<p>Wage Rp6,000,000, 5-day week, 9 hours of overtime on a Saturday. Hourly wage Rp34,682. Overtime pay = 8 × 2 × Rp34,682 + 1 × 3 × Rp34,682 = Rp554,913 + Rp104,046 = about <b>Rp658,960</b>.</p>
<p>Overtime pay is income subject to PPh 21, so that month's tax deduction may rise slightly.</p>"""),
      ("Tips to make sure overtime is paid correctly", "<ul>"
       "<li><b>Record start and end times</b> for every overtime session, and who instructed it.</li>"
       "<li><b>Ask for an overtime order</b> or written approval, including by email or attendance app.</li>"
       "<li><b>Check the overtime line on your payslip</b> and recalculate with the formula above.</li>"
       "<li><b>Know the exceptions</b>: for certain positions with high responsibility (such as managers), companies may set different terms as long as pay is higher; check your employment agreement.</li>"
       "<li>If there is a dispute, talk to HR or the union, then the local manpower office.</li></ul>"
       + TIP("enter your average monthly overtime pay as a variable allowance in the take-home pay calculator to see the effect on tax and net pay.")),
  ],
  faq=[("Can overtime be replaced with leave?", "The rules require overtime pay. Any other arrangement should not disadvantage the employee and should be clearly written."),
       ("Is overtime based on base salary only?", "It is based on monthly wages: base salary plus fixed allowances.")])

A("tips-negosiasi-gaji", slug="salary-negotiation-tips",
  title="Salary Negotiation Tips: Gross vs. Net, Benefits, and How to Ask",
  h1="Salary Negotiation Tips for a New Job",
  desc="How to negotiate salary in Indonesia: market research, understanding gross and net, valuing benefits, timing, and example phrases to use.",
  lead="The number you agree at the start becomes the base for raises for years to come. Prepare the negotiation well.",
  body=[
      ("Research before naming a number", """<p>Find the salary range for the same role, experience, industry, and city. Sources include recruitment agency salary reports, job ads that list pay, professional communities, or friends in the same industry. Set three numbers: your <b>ideal</b>, a <b>reasonable</b> figure, and the <b>minimum</b> you would accept.</p>"""),
      ("Understand gross and net", """<p>Make sure the number discussed is <b>gross</b> (before deductions) or <b>net</b> (what you receive). The difference can be hundreds of thousands to millions of rupiah a month because of BPJS and PPh 21. Also ask whether tax is borne by the company.</p>
<p>Ask for the breakdown of <b>base salary and fixed allowances</b>. These are the basis for THR, BPJS (including your JHT balance and pension), overtime, and severance. Offers with a large base salary are generally better in the long run than offers with large variable allowances.</p>"""),
      ("Value the benefits", """<ul><li>Private health insurance for you and your family.</li><li>Annual bonus: guaranteed or performance-based.</li>
<li>Transport, meal, communication, or remote-work allowances.</li><li>Flexible working and commute time; two hours of travel a day has a cost too.</li>
<li>Learning opportunities, certifications, and career path.</li></ul>
<p>Two offers with the same salary can be worth very different amounts once benefits are counted.</p>"""),
      ("How to ask", "<ul>"
       "<li><b>Let the company name a number first</b> if possible. If asked, give a range with the lower end slightly above your reasonable figure.</li>"
       "<li><b>Base it on value</b>, not personal needs: experience, results, and relevant skills.</li>"
       "<li><b>Be polite and clear</b>, for example: &ldquo;Based on my experience in this field and the market range for similar roles, I'm looking for Rp… to Rp… gross per month.&rdquo;</li>"
       "<li><b>Negotiate beyond salary</b> if the number is fixed: start date, remote days, a salary review after probation, or a training allowance.</li>"
       "<li><b>Get the offer in writing</b> with base salary, allowances, and benefits before resigning from your current job.</li></ul>"
       + TIP("calculate the take-home pay of each offer with the take-home pay calculator so you compare what you will actually receive.")),
  ],
  faq=[("What raise is reasonable when switching jobs?", "There is no fixed number. It depends on the market, seniority, and the company's needs. Market research is the best benchmark."),
       ("Can I decline to share my current salary?", "Yes. You can answer with your expected salary for the new role based on market research.")])

A("cara-membuat-anggaran-50-30-20", slug="50-30-20-budget-guide",
  title="How to Build a Monthly Budget with the 50/30/20 Rule",
  h1="How to Build a 50/30/20 Monthly Budget",
  desc="A guide to monthly budgeting with the 50/30/20 rule: splitting salary into needs, wants, and savings, with examples and tips to make it stick.",
  lead="The 50/30/20 rule is the simplest way to start managing your salary without tracking every rupiah.",
  body=[
      ("What is the 50/30/20 rule?", """<p>The rule splits your <b>net income</b> into three buckets:</p>
<ul><li><b>50% needs</b>: things you must pay, such as food, rent or mortgage, electricity, water, transport, internet, children's education, and minimum debt payments.</li>
<li><b>30% wants</b>: things that are nice but can be cut, such as eating out, entertainment, shopping, holidays, and subscriptions.</li>
<li><b>20% savings and investing</b>: emergency fund, long-term goals, and paying off debt faster.</li></ul>
[[CH_ANGGARAN]]"""),
      ("Steps to build your budget", """<ol><li><b>Calculate your average monthly net income</b>, after BPJS and tax.</li>
<li><b>Track spending for one or two months</b> using bank and e-wallet statements.</li>
<li><b>Group it</b> into needs, wants, and savings.</li>
<li><b>Compare</b> with 50/30/20 and decide which bucket needs to change.</li>
<li><b>Automate</b>: move 20% to a separate account on payday.</li></ol>"""),
      ("Adapting it to your situation", """<p>50/30/20 is a starting point, not a fixed rule. In big cities with high rent, needs may reach 60%; cut wants, not savings. If you have high-interest debt, use most of the 20% to pay it off first. When income rises, try to send the increase to savings rather than lifestyle.</p>"""),
      ("Tips to make the budget work", "<ul>"
       "<li><b>Separate accounts</b>: one for needs, one for daily spending, one for savings.</li>"
       "<li><b>Use digital envelopes</b> or savings pockets in your banking app.</li>"
       "<li><b>Review every month</b> for 10–15 minutes.</li>"
       "<li><b>Plan annual items</b> such as vehicle tax, insurance, and school fees by saving a little each month.</li>"
       "<li><b>Leave room for yourself.</b> Budgets that are too strict often fail by month two.</li></ul>"
       + TIP("start from an accurate net salary. The take-home pay calculator works it out after BPJS and PPh 21.")),
  ],
  faq=[("What if my income is irregular?", "Budget from your lowest month, then save the surplus in better months."),
       ("Are loan installments needs?", "Minimum installments are needs. Extra payments to clear debt faster can come from the 20%.")])

A("cara-cek-saldo-dan-klaim-jht", slug="check-and-claim-bpjs-jht",
  title="How to Check and Claim Your BPJS Employment JHT Balance: Requirements and Steps",
  h1="How to Check and Claim Your JHT Balance",
  desc="Guide to checking your JHT balance, JHT claim requirements when you stop working or for partial claims, documents needed, how to claim online, and tax on JHT.",
  lead="Your JHT balance is your own savings. Learn how to check and withdraw it so you don't miss what is yours.",
  body=[
      ("How to check your JHT balance", """<p>The easiest way is the official <b>JMO (Jamsostek Mobile)</b> app: register with your NIK and personal details, then view your balance and monthly contribution history. You can also check at a BPJS Employment branch office. Check at least every few months to make sure your employer actually pays contributions and reports the correct wage.</p>"""),
      ("When can JHT be withdrawn?", """<ul><li><b>When you stop working</b>, whether you resign or are laid off, after the waiting period set by the rules.</li>
<li><b>On reaching retirement age</b>.</li><li><b>Permanent total disability</b>.</li><li><b>Death</b>, paid to heirs.</li><li><b>Leaving Indonesia</b> permanently.</li>
<li><b>Partial claim</b> after at least 10 years of membership: up to 10% for retirement preparation or up to 30% for home ownership, while still employed. Only one partial claim option can be chosen.</li></ul>"""),
      ("Documents and how to claim", """<p>Documents commonly required: e-KTP, BPJS Employment membership card (or membership number), a letter of employment termination or reference letter (paklaring) from the employer, a savings book in your own name, and a tax ID (NPWP) if the balance exceeds a certain amount. Claims can be made through the JMO app, the online service on the official BPJS Employment website, or at a branch office. Follow the latest document list on official channels, as requirements can change.</p>"""),
      ("Tax on JHT", """<p>JHT paid as a lump sum is subject to final income tax: <b>0% up to Rp50 million</b> and <b>5% on the portion above Rp50 million</b>. The tax is deducted at payout.</p>"""),
      ("JHT tips", "<ul>"
       "<li><b>Use official channels only.</b> Beware of brokers or claim services that ask for personal data and fees.</li>"
       "<li><b>Ask for a paklaring</b> before your last working day.</li>"
       "<li><b>Changing jobs? Consider not withdrawing.</b> The balance can be merged into your membership at the new employer and keep growing.</li>"
       "<li><b>Match your data</b> (name, NIK, date of birth) in BPJS with your ID card so claims aren't delayed.</li></ul>"
       + TIP("see how much JHT is paid in each month for your wage with the BPJS contribution calculator.")),
  ],
  faq=[("How long does a JHT claim take?", "Usually a few working days after documents are complete and verified, depending on the channel and queue."),
       ("Is JHT different from the Pension (JP)?", "Yes. JHT is paid as a lump sum from your savings balance, while JP pays a monthly pension once the contribution period requirement is met.")])

A("pinjaman-online-vs-kredit-bank", slug="online-loans-vs-bank-loans",
  title="Online Loans vs. Bank Loans in Indonesia: Compare Costs and Risks",
  h1="Online Loans vs. Bank Loans: Which Is Safer?",
  desc="Compare online lending (pindar), paylater, credit cards, and bank personal loans: how to compare interest, signs of illegal lenders, and tips for borrowing safely.",
  lead="Online loans are fast, but they can be far more expensive. Compare before you choose.",
  body=[
      ("Types of loans", """<ul><li><b>Online lending (pindar)</b>: loans through apps of OJK-licensed platforms, fast disbursement, short terms.</li>
<li><b>Paylater</b>: buy-now-pay-later in shopping apps or e-wallets.</li>
<li><b>Credit cards</b>: revolving credit; interest applies if the bill is not paid in full.</li>
<li><b>Bank personal loans (KTA)</b>: unsecured loans with 1–5 year terms, stricter process, generally lower interest.</li></ul>"""),
      ("Compare in the same units", """<p>Online loan interest is often quoted <b>per day</b>, credit cards <b>per month</b>, and personal loans <b>per year</b>. Convert to the same unit before comparing. A rate of 0.2% per day, for example, equals about 6% per month or 73% per year.</p>
[[CH_PINJAM]]
<p>OJK caps the economic benefit (interest and fees) of online lending and has been lowering it gradually. Even so, for short-term borrowing the cost remains much higher than a bank loan.</p>"""),
      ("Signs of an illegal lender", """<ul><li>Not registered with OJK. Check the official list on the OJK website or call OJK on 157.</li>
<li>Unsolicited offers by SMS or WhatsApp.</li><li>Requests access to all your contacts, photos, or location.</li>
<li>Unclear interest and fees, very large upfront deductions.</li><li>Debt collection with threats or spreading your data.</li></ul>"""),
      ("Tips for borrowing safely", "<ul>"
       "<li><b>Borrow for needs, not lifestyle.</b> Avoid borrowing to repay another loan.</li>"
       "<li><b>Calculate the total repayment</b>, including service fees and penalties.</li>"
       "<li><b>Keep total installments</b> below 30% of income.</li>"
       "<li><b>Prefer bank credit</b> when time allows; it costs less.</li>"
       "<li><b>Pay on time.</b> Online loan and paylater history is recorded in SLIK OJK and affects mortgage and other loan applications.</li></ul>"
       + TIP("to compare flat and effective interest, use the vehicle loan calculator; the same principle applies to other fixed-installment loans.")),
  ],
  faq=[("Does paylater affect a mortgage application?", "It can. Paylater from licensed providers is recorded in SLIK OJK. Arrears can cause other loan applications to be rejected."),
       ("What if I am already trapped by an illegal lender?", "Don't take new loans. Report it to OJK and the PASTI task force, and to the police if there are threats or data leaks.")])

A("take-over-dan-pelunasan-kpr", slug="mortgage-refinancing-and-early-repayment",
  title="Mortgage Take Over and Early Repayment in Indonesia: When Does It Pay Off?",
  h1="KPR Take Over and Early Repayment",
  desc="How refinancing a KPR to another bank and partial or full prepayment work: calculating savings, costs to consider, and tips on timing.",
  lead="When floating rates feel heavy, there are two ways to lighten a mortgage: move to another bank or pay part of it off early.",
  body=[
      ("What is a KPR take over?", """<p>A <b>take over</b> means a new bank pays off your remaining KPR, and you continue paying the new bank at a new rate and term. The goal is usually a lower rate, such as a promotional fixed rate, or a different term for lighter installments.</p>
[[CH_TAKEOVER]]"""),
      ("Costs to include", """<ul><li><b>Prepayment penalty</b> at the old bank, usually a percentage of remaining principal, especially during the fixed period.</li>
<li><b>Provision and admin fees</b> at the new bank.</li><li><b>Property appraisal</b>.</li><li><b>Notary</b> for releasing the old mortgage (roya) and a new APHT.</li>
<li>New <b>life and fire insurance</b>.</li></ul>
<p>A take over pays off when <b>total interest savings are much larger than total costs</b>. Remember that the new bank's promotional rate only lasts a few years.</p>"""),
      ("Partial or full prepayment", """<p>If you have extra money, for example from a bonus, you can pay down part of the principal. Afterwards you can choose <b>lower installments</b> with the same term, or a <b>shorter term</b> with the same installment. Shortening the term usually saves more interest.</p>
<p>Prepayment is most effective in the <b>early years</b> and when floating rates are high, because the interest portion is still large. Ask the bank about penalties and minimum prepayment amounts.</p>"""),
      ("Tips for deciding", "<ul>"
       "<li><b>Calculate the break-even point</b>: how many months of installment savings cover the take-over costs.</li>"
       "<li><b>Don't use your emergency fund</b> to prepay a mortgage.</li>"
       "<li><b>Compare with investing</b>: if the mortgage rate is higher than a realistic net investment return, prepaying tends to be better.</li>"
       "<li><b>Keep your credit history clean</b>; the new bank will check SLIK OJK.</li>"
       "<li><b>Ask for written simulations</b> from both banks.</li></ul>"
       + TIP("use the mortgage calculator to work out the new installment with the remaining principal, rate, and remaining term after a take over.")),
  ],
  faq=[("When is the best time to take over?", "Usually after the fixed period ends, since penalties are typically higher during it, and when the rate gap is wide enough."),
       ("Can a sharia KPR be taken over?", "Yes, to another sharia or conventional bank, with different cost calculations and contracts.")])

A("mengenal-sbn-ritel", slug="retail-government-bonds-sbn",
  title="Retail Government Bonds in Indonesia (SBN): ORI, Retail Sukuk, SBR, and Savings Sukuk",
  h1="Retail Government Bonds (SBN) for Beginner Investors",
  desc="An explanation of Indonesian retail government securities: ORI, SR, SBR, and ST, tradable vs. non-tradable, coupon tax, how to buy, and tips for choosing.",
  lead="Retail SBN are government bonds individuals can buy from small amounts, with returns guaranteed by the state.",
  body=[
      ("What are retail SBN?", """<p><b>Retail Government Securities (SBN ritel)</b> are issued by the government for the public. You lend money to the state and receive a <b>coupon</b> periodically, then get your principal back at maturity. Coupon and principal payments are guaranteed by law, so default risk is very low.</p>"""),
      ("Types of retail SBN", """<div class="tscroll"><table class="tbl"><thead><tr><th>Type</th><th>Principle</th><th>Coupon</th><th>Can be sold before maturity?</th></tr></thead><tbody>
<tr><td>ORI (Retail Government Bond)</td><td>Conventional</td><td>Fixed</td><td>Yes, on the secondary market</td></tr>
<tr><td>SR (Retail Sukuk)</td><td>Sharia</td><td>Fixed</td><td>Yes, on the secondary market</td></tr>
<tr><td>SBR (Savings Bond Ritel)</td><td>Conventional</td><td>Floating with a floor</td><td>No; partial early redemption available</td></tr>
<tr><td>ST (Savings Sukuk)</td><td>Sharia</td><td>Floating with a floor</td><td>No; partial early redemption available</td></tr></tbody></table></div>
<p>Tradable series can rise or fall in price on the secondary market, so you may gain or lose if you sell before maturity. Non-tradable series keep their value, but early redemption is only possible on set dates.</p>"""),
      ("Tax and how to buy", """<p>SBN coupons are subject to a <b>10% final tax</b>, lower than the 20% tax on deposit interest. Retail SBN are sold during set offering periods several times a year through <b>official distribution partners</b> appointed by the Ministry of Finance, such as banks, brokers, and investment platforms. The minimum purchase usually starts at Rp1 million.</p>"""),
      ("Tips for investing in retail SBN", "<ul>"
       "<li><b>Match the tenor to your goal</b>, usually 2–6 years.</li>"
       "<li><b>Choose a fixed coupon</b> if you expect rates to fall, and a <b>floating coupon</b> if you expect rates to rise.</li>"
       "<li><b>Buy from official distribution partners</b>; check the list on the Ministry of Finance website.</li>"
       "<li><b>Note the offering dates</b>; quotas can run out quickly.</li>"
       "<li><b>Make it part of a portfolio</b>, together with an emergency fund and other long-term instruments.</li></ul>"
       + TIP("simulate returns at a given coupon in the investment calculator, then compare with a deposit in the deposit calculator.")),
  ],
  faq=[("Are retail SBN safe?", "Coupon and principal payments are guaranteed by the state. The remaining risk is price changes if a tradable series is sold before maturity."),
       ("Are retail SBN suitable for an emergency fund?", "Not really, because you can't always cash out at any time. Keep emergency funds in more liquid instruments.")])

A("reksa-dana-vs-deposito", slug="mutual-funds-vs-time-deposits",
  title="Mutual Funds vs. Time Deposits: Differences, Risk, Tax, and Which Suits You",
  h1="Mutual Funds vs. Time Deposits: Which Suits You?",
  desc="Compare mutual funds and time deposits in Indonesia by return, risk, tax, liquidity, and guarantee, with guidance on choosing by financial goal.",
  lead="Deposits and mutual funds are both popular ways to grow money, but they work differently and carry different risks.",
  body=[
      ("Key differences", """<div class="tscroll"><table class="tbl"><thead><tr><th>Aspect</th><th>Time deposit</th><th>Mutual fund</th></tr></thead><tbody>
<tr><td>Type</td><td>Bank deposit</td><td>Investment managed by an investment manager</td></tr>
<tr><td>Return</td><td>Fixed interest from the start</td><td>Not fixed, follows asset values</td></tr>
<tr><td>Guarantee</td><td>LPS up to Rp2 billion (with conditions)</td><td>Not guaranteed; supervised by OJK, assets held by a custodian bank</td></tr>
<tr><td>Tax for you</td><td>Interest subject to 20% final tax</td><td>Gains are not taxable for the investor (tax at portfolio level)</td></tr>
<tr><td>Withdrawal</td><td>At maturity; earlier may be penalized</td><td>Any exchange day; funds arrive in a few working days</td></tr>
<tr><td>Minimum</td><td>Usually millions of rupiah</td><td>Can start from tens of thousands of rupiah</td></tr></tbody></table></div>"""),
      ("Types of mutual funds", """<ul><li><b>Money market</b>: deposits and short-term debt. Lowest risk, suitable for needs within 1 year.</li>
<li><b>Fixed income</b>: bonds. Suitable for 1–3 years.</li><li><b>Balanced</b>: a mix of stocks and bonds.</li>
<li><b>Equity</b>: highest potential, largest swings. Suitable for 5 years or more.</li></ul>"""),
      ("Choosing by goal", """<ul><li><b>Emergency fund</b>: savings and money market funds, because they are easy to withdraw.</li>
<li><b>Fixed goals in 1–2 years</b> (house down payment, wedding): deposits, money market, or fixed income funds.</li>
<li><b>Long-term goals</b> (retirement, children's education): regular investing in equity or balanced funds, together with SBN.</li></ul>"""),
      ("Tips for choosing", "<ul>"
       "<li><b>Compare net returns</b>: deposit interest after 20% tax versus fund performance after fees.</li>"
       "<li><b>Make sure products and apps are registered with OJK.</b></li>"
       "<li><b>Look at long-term performance</b>, not just last month, and read the prospectus or fund fact sheet.</li>"
       "<li><b>Watch fees</b> for buying, selling, and management.</li>"
       "<li><b>You don't have to pick one.</b> A mix that matches your goals is often best.</li></ul>"
       + TIP("calculate net deposit interest with the deposit calculator as a benchmark for mutual fund returns.")),
  ],
  faq=[("Can mutual funds lose money?", "Yes. Unit values can fall, especially for equity funds. Money market funds are the most stable but still not guaranteed."),
       ("Do I report mutual fund gains in my tax return?", "Mutual fund gains are not taxable for the investor, but the investment value is reported as an asset.")])

A("berapa-dana-darurat-yang-ideal", slug="how-big-should-your-emergency-fund-be",
  title="How Big Should Your Emergency Fund Be, and Where Should You Keep It?",
  h1="How Big Should Your Emergency Fund Be?",
  desc="Emergency fund guide: what it is, how to calculate the ideal amount for your situation, where to keep it, and how to build one from zero.",
  lead="An emergency fund is the foundation of your finances. Without it, one unexpected event can force you into debt.",
  body=[
      ("What is an emergency fund?", """<p>An <b>emergency fund</b> is money set aside specifically for unexpected events: losing your job, illness, vehicle or home repairs, or urgent family needs. It is <b>not</b> for holidays, sales, or investing.</p>"""),
      ("How much is ideal?", """<p>The usual benchmark is based on <b>essential monthly expenses</b>, not salary:</p>
<ul><li>Single: 3–6 months of expenses.</li><li>Married: 6 months.</li><li>Married with children: 9 months or more.</li>
<li>Self-employed, freelancers, or irregular income: 12 months.</li></ul>
[[CH_DARURAT]]"""),
      ("Where to keep it", """<p>An emergency fund must be <b>safe</b> and <b>easy to access</b>, not chasing high returns:</p>
<ul><li><b>A separate savings account</b>, for needs that can arise the same day.</li>
<li><b>Money market funds</b>, withdrawable within a few working days.</li>
<li><b>Short-term or laddered deposits</b> for part of the fund.</li></ul>
<p>Avoid stocks, crypto, or property for emergency funds, because their value can fall just when you need the money.</p>"""),
      ("Building one from zero", "<ol>"
       "<li><b>Calculate essential monthly expenses</b> and set a target.</li>"
       "<li><b>Start with a small target</b>, such as one month of expenses, then raise it gradually.</li>"
       "<li><b>Save automatically</b> on payday, for example 10–20% of net salary.</li>"
       "<li><b>Use extra income</b> such as THR or bonuses to speed it up.</li>"
       "<li><b>Top it back up</b> whenever you use it.</li></ol>"
       + TIP("keep part of your emergency fund in laddered deposits and calculate the net interest with the deposit calculator.")),
  ],
  faq=[("Do I need an emergency fund if I have insurance?", "Yes. Insurance covers specific risks, while an emergency fund covers other urgent needs such as lost income."),
       ("Emergency fund or investing first?", "Usually the emergency fund first, at least partly, so you don't have to sell investments when prices are down.")])
