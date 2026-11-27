"""English content for GetWise: categories, calculators (forms + articles), and static pages.
Field ids in the forms must match the Indonesian version because the page scripts read them."""
from content import chk, money, num, sel

STATUS_EN = [("TK/0", "TK/0 – single, no dependants"), ("TK/1", "TK/1 – single, 1 dependant"), ("TK/2", "TK/2 – single, 2 dependants"),
             ("TK/3", "TK/3 – single, 3 dependants"), ("K/0", "K/0 – married, no dependants"), ("K/1", "K/1 – married, 1 dependant"),
             ("K/2", "K/2 – married, 2 dependants"), ("K/3", "K/3 – married, 3 dependants")]
JKK_EN = [("sangat_rendah", "Very low – 0.24% (office, services)"), ("rendah", "Low – 0.54%"), ("sedang", "Medium – 0.89%"),
          ("tinggi", "High – 1.27%"), ("sangat_tinggi", "Very high – 1.74% (mining, heavy construction)")]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

BPJS_OPTS_EN = ('<div class="fld"><label>BPJS programs enrolled</label>' + chk("kes", "BPJS Health (Kesehatan)") + chk("jht", "JHT (Old-Age Savings)")
                + chk("jp", "JP (Pension)") + chk("jkkjkm", "JKK &amp; JKM (paid by employer)") + "</div>"
                + sel("jkk", "Work-accident risk level (JKK)", JKK_EN, "sangat_rendah"))

CATS_EN = {
    "pajak-gaji": dict(short="Tax & Salary", name="Tax & Salary", desc="PPh 21 (TER method), take-home pay, and THR"),
    "bpjs": dict(short="BPJS", name="BPJS & Social Security", desc="BPJS Health and Employment contributions"),
    "kredit": dict(short="Loans", name="Loans & Installments", desc="Mortgages (KPR) and vehicle loans"),
    "investasi": dict(short="Investing", name="Savings & Investing", desc="Time deposits and regular investing"),
}

SRC_TER = ("Directorate General of Taxes – About the PPh 21 TER method", "https://pajak.go.id/id/artikel/serba-serbi-ter-pph-pasal-21-pajak-baru-atau-formula-baru")
SRC_TER2 = ("Directorate General of Taxes – TER explained", "https://www.pajak.go.id/id/artikel/simpel-pakai-ter-begini-penjelasannya")
SRC_PP58 = ("Government Regulation (PP) 58/2023 on PPh 21 withholding rates and Minister of Finance Regulation (PMK) 168/2023", "")
SRC_HPP = ("Law 7/2021 on Harmonization of Tax Regulations (HPP), Article 17 rates", "")
SRC_BPJSTK = ("BPJS Ketenagakerjaan – JHT, JKK, JKM, JP, and JKP contribution rates", "https://www.bpjsketenagakerjaan.go.id/artikel/18913/artikel-berapa-besaran-iuran-jht-jkk-jkm-jp-dan-jkp")
SRC_KES = ("Presidential Regulation 64/2020 on Health Insurance (5% contribution, Rp12 million wage cap)", "")
SRC_JP = ("2026 pension (JP) wage cap: Rp11,086,300 from March 2026 (previously Rp10,547,400)", "https://www.mondaq.com/employee-benefits-compensation/1756368/socialization-of-pension-wage-limit-regulations-for-the-year-2026-indonesia")

CALC_EN = {}

CALC_EN["pph21"] = dict(
    short="PPh 21 Calculator", chip="PPh 21",
    title="PPh 21 Calculator 2026 (TER Method) – Indonesian Income Tax on Salary",
    h1="Indonesian Income Tax (PPh 21) Calculator 2026 – TER Method",
    desc="Calculate Indonesian employee income tax (PPh 21) with the average effective rate (TER) under PP 58/2023: monthly withholding for January–November, December reconciliation, PTKP, and job expense deduction.",
    card="Monthly salary tax with TER and the December reconciliation.",
    lead="Estimate the PPh 21 withheld from a permanent employee's salary each month using the average effective rate (TER), including the December recalculation under the Article 17 progressive rates.",
    form=money("gaji", "Base salary + fixed allowances / month", "10000000", "Regular monthly income before deductions.")
    + money("tidakTetap", "Variable allowances / month", "0", "Overtime, incentives, daily meal allowance (monthly average).")
    + sel("status", "PTKP status", STATUS_EN, "TK/0", "Your status at the start of the tax year.")
    + money("bonus", "Bonus / THR per year", "0", "One-off, non-regular income.")
    + sel("bulanBonus", "Month the bonus is paid", [(i + 1, b) for i, b in enumerate(MONTHS)], 4),
    opts=BPJS_OPTS_EN,
    sections=[
        ("How PPh 21 is calculated with TER", """<p>Since 1 January 2024, PPh 21 for permanent employees has been withheld using the <b>average effective rate (TER)</b> under PP 58/2023 and PMK 168/2023. The calculation has two parts:</p>
<ol><li><b>January to November</b>: PPh 21 = <b>gross income for that month × TER rate</b>. The rate comes from table A, B, or C depending on your PTKP status and that month's gross income.</li>
<li><b>December (last tax period)</b>: the full-year tax is recalculated with the progressive Article 17 rates, minus what was withheld from January to November. The difference is December's deduction; if negative, the excess is refunded.</li></ol>
<p>That is why the December deduction often differs from other months, especially if you received a bonus, THR, or a raise during the year.</p>"""),
        ("What counts as gross income?", """<p>Gross income is more than your base salary. It includes:</p>
<ul><li>base salary, fixed allowances, and variable allowances (overtime, incentives);</li>
<li>bonuses, THR, and other irregular income in the month they are paid;</li>
<li><b>insurance premiums paid by the employer</b>: the employer's share of BPJS Health (4%), JKK, and JKM. You do not receive this in cash, but it is added to gross income.</li></ul>
<p>The employer's JHT and JP contributions are <b>not</b> added. This calculator handles all of this automatically based on the BPJS programs selected in the advanced settings.</p>"""),
        ("TER categories and PTKP", """<p>The TER category follows your PTKP status:</p>
<ul><li><b>Category A</b>: TK/0, TK/1, K/0 (PTKP Rp54 million to Rp58.5 million)</li>
<li><b>Category B</b>: TK/2, TK/3, K/1, K/2 (PTKP Rp63 million to Rp67.5 million)</li>
<li><b>Category C</b>: K/3 (PTKP Rp72 million)</li></ul>
<p>Annual PTKP (non-taxable income): Rp54,000,000 for the taxpayer, plus Rp4,500,000 if married, and Rp4,500,000 for each dependant (maximum three).</p>"""),
        ("The December calculation (Article 17 rates)", """<div class="formula">Annual gross income
− Job expense deduction (5%, max. Rp6,000,000 per year)
− Employee JHT 2% and JP 1% contributions
= Annual net income
− PTKP
= Taxable income (PKP, rounded down to the nearest thousand)
Annual PPh 21 = Article 17 rates × PKP
December PPh 21 = annual PPh 21 − PPh 21 withheld January–November</div>
<p>Article 17 rates (HPP Law): 5% up to Rp60 million; 15% above Rp60 million to Rp250 million; 25% above Rp250 million to Rp500 million; 30% above Rp500 million to Rp5 billion; 35% above Rp5 billion.</p>"""),
        ("Example", """<p>An employee with TK/0 status earns Rp10,000,000 a month, with no BPJS and no bonus. Gross income of Rp10,000,000 falls in the TER category A bracket above Rp9,650,000 up to Rp10,050,000, with a 2% rate. Withholding for January–November is Rp200,000 a month, Rp2,200,000 in total.</p>
<p>In December: annual gross Rp120,000,000 − job expense Rp6,000,000 = net Rp114,000,000; minus PTKP Rp54,000,000 gives PKP of Rp60,000,000; annual tax 5% × Rp60,000,000 = Rp3,000,000. December deduction = Rp3,000,000 − Rp2,200,000 = <b>Rp800,000</b>.</p>"""),
    ],
    faq=[("Why is my December deduction larger than usual?", "TER is an approximation. In December the full-year tax is recalculated with the progressive Article 17 rates, so any under-withholding from January–November is collected at once. Bonuses or mid-year raises widen the gap."),
         ("Does TER increase my annual tax?", "No. TER only changes how tax is withheld each month. The total annual tax is still determined by the Article 17 calculation in the last tax period."),
         ("What if I leave my job mid-year?", "Your last month of work is treated like December: tax is recalculated under Article 17 for your annualized income according to the rules. This calculator assumes you work the full January–December period."),
         ("Does the employee's 1% BPJS Health contribution reduce tax?", "No. Only the employee's JHT and JP contributions and the job expense deduction reduce taxable income."),
         ("Which status determines the TER category?", "Your PTKP status at the start of the tax year (or when you start working). A change during the year, such as getting married, applies from the next tax year.")],
    sources=[SRC_TER, SRC_TER2, SRC_PP58, SRC_HPP, SRC_BPJSTK],
)

CALC_EN["gaji-bersih"] = dict(
    short="Take-Home Pay Calculator", chip="Take-Home Pay",
    title="Indonesia Take-Home Pay Calculator 2026 – Net Salary After BPJS & PPh 21",
    h1="Indonesia Take-Home Pay (Net Salary) Calculator 2026",
    desc="Calculate your net salary in Indonesia after BPJS Health, JHT, JP, and PPh 21 (TER) deductions, plus the total cost to the employer.",
    card="What actually lands in your account after BPJS and PPh 21.",
    lead="From gross salary to the amount in your bank account: BPJS Health, JHT, JP, and PPh 21 deductions are calculated automatically, along with the total cost borne by the employer.",
    form=money("gaji", "Base salary + fixed allowances / month", "8000000") + money("tidakTetap", "Variable allowances / month", "0", "Overtime, incentives, daily transport allowance.")
    + sel("status", "PTKP status", STATUS_EN, "TK/0"),
    opts=BPJS_OPTS_EN,
    sections=[
        ("Salary deductions in Indonesia", """<p>Take-home pay is your gross salary minus three groups of mandatory deductions:</p>
<ul><li><b>BPJS Health 1%</b> of wages, capped at a Rp12 million wage (the employer pays 4%).</li>
<li><b>JHT 2%</b> of wages with no cap (the employer pays 3.7%).</li>
<li><b>JP 1%</b> of wages, capped at Rp11,086,300 from March 2026 (the employer pays 2%).</li>
<li><b>PPh 21</b> withheld with the TER method for January–November.</li></ul>
<p>Other deductions such as cooperative dues, staff loans, or union fees are not included because they differ between companies.</p>"""),
        ("Normal-month net pay vs. annual average", """<p>The calculator shows two figures. <b>Normal-month take-home pay</b> uses the TER tax withheld from January to November. The <b>annual average</b> uses the actual annual tax divided by 12, because December's deduction can be higher or lower. The second figure is better for monthly budgeting.</p>"""),
        ("Cost to the employer", """<p>For a company, an employee costs more than the gross salary because of the employer's BPJS contributions: Health 4%, JHT 3.7%, JP 2%, JKK 0.24% to 1.74% depending on risk, and JKM 0.3%. This figure is useful for business owners budgeting payroll.</p>"""),
        ("Example", """<p>Salary Rp8,000,000, status TK/0, enrolled in all BPJS programs with very low risk. Employee deductions: BPJS Health Rp80,000, JHT Rp160,000, JP Rp80,000. Gross for tax = Rp8,000,000 + premiums paid by the employer (Health Rp320,000, JKK Rp19,200, JKM Rp24,000) = Rp8,363,200, TER category A rate 1.5%, so PPh 21 is Rp125,448. Normal-month take-home pay is about <b>Rp7,554,552</b>.</p>"""),
    ],
    faq=[("Why do the employer's BPJS premiums increase my tax?", "Under the rules, health, work-accident, and death insurance premiums paid by the employer count as the employee's gross income, even though they are not received in cash."),
         ("What if my employer pays my tax (gross-up or borne by employer)?", "If the company bears your tax, your take-home pay equals gross salary minus BPJS. This calculator uses the common scheme where tax is deducted from salary."),
         ("Are meal and transport allowances taxable?", "If paid in cash, yes, they are part of gross income. Enter the monthly average in the variable allowances field."),
         ("Are BPJS contributions based on base salary only?", "BPJS contributions are based on wages: base salary plus fixed allowances. This calculator uses the base salary + fixed allowances field as the contribution base.")],
    sources=[SRC_BPJSTK, SRC_KES, SRC_JP, SRC_TER, SRC_PP58],
)

CALC_EN["thr"] = dict(
    short="THR Calculator", chip="THR",
    title="THR Calculator 2026 – Indonesian Religious Holiday Allowance & Its Tax",
    h1="THR (Religious Holiday Allowance) Calculator 2026",
    desc="Calculate your THR entitlement based on length of service (full or pro-rata) and the estimated PPh 21 TER deduction in the month it is paid.",
    card="Full or pro-rata THR, plus the tax deducted.",
    lead="Work out your THR entitlement based on length of service, then see how much extra PPh 21 is withheld in the month THR is paid and how much THR you actually receive.",
    form=money("gaji", "Base salary + fixed allowances / month", "8000000", "THR is based on wages: base salary plus fixed allowances.")
    + num("masaKerja", "Length of service (months)", "12", "months", "Counted up to the religious holiday.") + sel("status", "PTKP status", STATUS_EN, "TK/0"),
    opts=money("tidakTetap", "Variable allowances / month", "0") + BPJS_OPTS_EN,
    sections=[
        ("Who is entitled and how much", """<p>Under Minister of Manpower Regulation 6/2016, employees with at least <b>1 month of continuous service</b> are entitled to a Religious Holiday Allowance (THR), whether permanent (PKWTT) or fixed-term (PKWT).</p>
<ul><li>Service of <b>12 months or more</b>: THR = 1 month's wages.</li>
<li>Service of <b>1 to less than 12 months</b>: THR = months of service ÷ 12 × 1 month's wages.</li></ul>
<p>Wages here means base salary plus fixed allowances. THR must be paid no later than 7 days before the holiday, and employers may pay more if set out in the employment agreement or company practice.</p>"""),
        ("Why is the tax so high in the THR month?", """<p>With the TER method, tax for the month is based on <b>that month's gross income</b>, which includes THR. Higher gross income falls into a higher TER bracket, so the deduction jumps.</p>
<p>The jump is not a permanent extra tax. In December the full-year tax is recalculated under Article 17, so the December deduction adjusts. Total annual tax is generally the same regardless of when THR is paid.</p>"""),
        ("Example", """<p>Salary Rp8,000,000, 6 months of service, status K/1, no BPJS. THR = 6/12 × Rp8,000,000 = Rp4,000,000. Normal month: gross Rp8,000,000 at TER category B 1% = Rp80,000. THR month: gross Rp12,000,000 at 3% = Rp360,000. The extra deduction from THR is Rp280,000, so net THR is about <b>Rp3,720,000</b>.</p>"""),
    ],
    faq=[("Are contract employees entitled to THR?", "Yes. PKWT (fixed-term) employees with at least 1 month of continuous service are entitled to THR."),
         ("What if I leave before the holiday?", "Permanent employees whose employment ends within 30 days before the holiday are still entitled to THR. For fixed-term employees whose contract ends before the holiday, the rules differ; check your employment agreement."),
         ("Is THR always taxed?", "THR is part of gross income and subject to PPh 21. If your annual income is below PTKP, the tax is refunded or not due in the December calculation."),
         ("Is THR based on base salary only?", "It is based on wages, meaning base salary plus fixed allowances. Variable allowances such as overtime are not included.")],
    sources=[("Minister of Manpower Regulation 6/2016 on Religious Holiday Allowance", ""), SRC_TER, SRC_PP58],
)

CALC_EN["bpjs"] = dict(
    short="BPJS Contribution Calculator", chip="BPJS",
    title="BPJS Contribution Calculator 2026 – Health & Employment (JHT, JP, JKK, JKM)",
    h1="BPJS Contribution Calculator 2026",
    desc="Calculate BPJS Health and BPJS Employment (JHT, JP, JKK, JKM) contributions for the employee and employer, with the latest wage caps.",
    card="Health, JHT, JP, JKK, JKM: employee and employer shares.",
    lead="Calculate monthly BPJS Health and BPJS Employment contributions, split between the part deducted from the employee's salary and the part paid by the employer.",
    form=money("gaji", "Monthly wage", "8000000", "Base salary + fixed allowances.") + BPJS_OPTS_EN,
    sections=[
        ("BPJS contribution rates for salaried workers", """<div class="tscroll"><table class="tbl"><thead><tr><th>Program</th><th>Employer</th><th>Employee</th><th>Wage cap</th></tr></thead><tbody>
<tr><td>BPJS Health</td><td>4%</td><td>1%</td><td>Rp12,000,000</td></tr>
<tr><td>JHT (Old-Age Savings)</td><td>3.7%</td><td>2%</td><td>none</td></tr>
<tr><td>JP (Pension)</td><td>2%</td><td>1%</td><td>Rp11,086,300 (from March 2026)</td></tr>
<tr><td>JKK (Work Accident)</td><td>0.24%–1.74%</td><td>–</td><td>none</td></tr>
<tr><td>JKM (Death)</td><td>0.3%</td><td>–</td><td>none</td></tr></tbody></table></div>
<p>Job Loss Insurance (JKP) adds no extra contribution because it is funded by the government and a recomposition of existing contributions.</p>"""),
        ("Wage caps and floors", """<p>For BPJS Health, wages above Rp12,000,000 are counted as Rp12,000,000, and reported wages may not be below the local minimum wage. For JP, the wage cap is updated every March in line with economic growth; from March 2026 it is Rp11,086,300, so the employee's maximum JP contribution is about Rp110,863 a month.</p>
<p>The employee's 1% BPJS Health contribution covers the member, spouse, and up to three children. Additional family members (for example a fourth child or parents) cost an extra 1% each.</p>"""),
        ("Example", """<p>Wage Rp8,000,000 with very low work risk. Employee share: Health Rp80,000, JHT Rp160,000, JP Rp80,000, total Rp320,000. Employer share: Health Rp320,000, JHT Rp296,000, JP Rp160,000, JKK Rp19,200, JKM Rp24,000, total Rp819,200.</p>"""),
    ],
    faq=[("Do BPJS contributions reduce tax?", "The employee's JHT 2% and JP 1% contributions reduce taxable income. The employee's BPJS Health contribution does not. Conversely, Health, JKK, and JKM premiums paid by the employer are added to gross income for PPh 21."),
         ("What if my salary is above Rp12 million?", "BPJS Health is calculated on Rp12,000,000, so the maximum employee deduction is Rp120,000 a month. JHT is still calculated on the full wage."),
         ("What about self-employed workers?", "Self-employed members pay under a different scheme (a fixed amount per class for Health, and based on declared income for Employment). This calculator is for salaried employees only."),
         ("When can JHT be withdrawn?", "JHT can be withdrawn at retirement age (56), on permanent total disability, death, or when you stop working under the applicable rules. Part of the balance can also be claimed early for certain purposes.")],
    sources=[SRC_BPJSTK, SRC_KES, SRC_JP, ("PP 44/2015 (JKK & JKM), PP 45/2015 (JP), PP 46/2015 (JHT), PP 37/2021 as amended by PP 6/2025 (JKP)", "")],
)

CALC_EN["kpr"] = dict(
    short="Mortgage (KPR) Calculator", chip="Mortgage",
    title="Indonesia Mortgage (KPR) Calculator 2026 – Fixed & Floating Rate Installments",
    h1="Mortgage (KPR) Calculator: Fixed and Floating Rates",
    desc="Calculate Indonesian mortgage (KPR) installments with a fixed rate followed by a floating rate (annuity method), total interest, yearly remaining principal, and the minimum income banks usually require.",
    card="Home loan installments with a fixed then floating rate, plus a yearly schedule.",
    lead="Simulate a KPR with a fixed-rate period followed by a floating rate. See the monthly installment, total interest, remaining principal each year, and the minimum income banks usually require.",
    form=money("harga", "House price", "600000000") + num("dpPersen", "Down payment", "20", "%") + num("tenorTahun", "Loan term", "15", "years")
    + num("fixTahun", "Fixed-rate period", "3", "years") + num("bungaFix", "Fixed rate per year", "4.5", "%") + num("bungaFloat", "Expected floating rate per year", "11", "%", "Rate after the fixed period ends."),
    sections=[
        ("How banks calculate KPR installments", """<p>Almost all mortgages in Indonesia use the <b>annuity method</b>: the monthly installment stays the same as long as the interest rate does not change, but the interest portion is large at the start and the principal portion is large at the end.</p>
<div class="formula">Installment = P × r ÷ (1 − (1 + r)^−n)
P = loan principal (price − down payment)
r = annual rate ÷ 12
n = remaining term in months</div>
<p>When the fixed period ends, the bank recalculates the installment with the same formula using the <b>remaining principal</b>, the <b>floating rate</b>, and the <b>remaining term</b>. Because floating rates are usually much higher, installments can jump sharply.</p>"""),
        ("Fixed, floating, and the risk of a payment jump", """<p>Promotional fixed rates (for example 3–5% for 1–5 years) keep early installments light. After that, the rate follows the bank's reference rate (floating), which can go up or down. Run several floating-rate scenarios, such as 10%, 12%, and 13%, to make sure you can still pay if rates rise.</p>"""),
        ("Minimum income and other costs", """<p>Banks generally require installments of no more than about <b>30–35% of monthly income</b> (joint income of a couple can count). This calculator shows the minimum income based on 30% of the highest installment.</p>
<p>Besides the down payment, prepare upfront costs such as bank provision and admin fees, notary and deed fees, life and fire insurance, and the buyer's tax (BPHTB). Amounts vary by bank and region; roughly a few percent of the house price.</p>"""),
        ("Tips to save on interest", """<ul><li>Increase the down payment to reduce the principal.</li><li>Choose the shortest term that is still comfortable; total interest drops dramatically.</li>
<li>Make partial prepayments when floating rates are high, keeping early-repayment penalties in mind.</li><li>Consider refinancing (take over) to another bank if the rate difference is large enough.</li></ul>"""),
    ],
    faq=[("What is the minimum down payment for a KPR?", "It is set by each bank under Bank Indonesia's loan-to-value (LTV) rules and current programs; some first-home programs allow a very small down payment. Ask the bank directly."),
         ("Why does the principal fall so slowly in the first years?", "With the annuity method, interest is calculated on the still-large remaining principal, so most early installments go to interest."),
         ("Will the result match the bank exactly?", "Close. Banks may use different rounding, day counts, or insurance costs included in the installment, so numbers can differ slightly."),
         ("Short or long term?", "A short term means higher installments but much less total interest. A long term means lighter installments but far more interest. Choose the shortest term whose installment stays below about 30% of income.")],
    sources=[("Standard bank annuity formula; Bank Indonesia LTV/FTV rules", "")],
)

CALC_EN["kredit-kendaraan"] = dict(
    short="Car & Motorcycle Loan Calculator", chip="Vehicle Loan",
    title="Car & Motorcycle Loan Calculator Indonesia – Flat Rate to Effective Rate",
    h1="Car and Motorcycle Loan Calculator",
    desc="Calculate vehicle loan installments with a flat rate, total interest, and the true effective annual rate to compare financing offers in Indonesia.",
    card="Flat-rate installments and the real effective rate.",
    lead="Calculate car or motorcycle loan installments with a flat rate, then see the true effective annual rate so you can compare offers fairly.",
    form=money("harga", "Vehicle price (on the road)", "30000000") + num("dpPersen", "Down payment", "20", "%") + num("tenorBulan", "Loan term", "36", "months")
    + num("bungaFlat", "Flat rate per year", "6", "%"),
    sections=[
        ("What is a flat rate?", """<p>Vehicle financing companies (leasing) in Indonesia usually use a <b>flat rate</b>: interest is calculated on the original principal for the whole term, even though the principal decreases every month.</p>
<div class="formula">Total interest = Principal × flat rate per year × term (years)
Installment = (Principal + Total interest) ÷ term (months)</div>"""),
        ("Why look at the effective rate?", """<p>Because a flat rate is charged on the original principal, the real cost is much higher than the advertised figure. The <b>effective rate</b> is the rate that produces the same installment when calculated on the remaining principal (like a mortgage). As a rough guide, a 6% flat rate over 3 years equals about 11% effective per year.</p>
<p>Use the effective rate to compare leasing offers with bank personal loans (KTA) or other borrowing.</p>"""),
        ("Other costs to consider", """<ul><li>Admin and provision fees upfront.</li><li>Vehicle insurance (comprehensive or total loss only), often included in the installment.</li>
<li>Late-payment fines and early-repayment penalties.</li><li>Fiduciary registration fees.</li></ul>
<p>Ask for the total payment (down payment + all installments + fees) in writing before signing.</p>"""),
    ],
    faq=[("Which is cheaper: a bigger down payment or a longer term?", "A bigger down payment and a shorter term are almost always cheaper, because total interest depends on the principal and the loan duration."),
         ("Can I repay early?", "Usually yes, but some lenders charge a penalty. Because flat interest is calculated upfront, check how the remaining interest is computed when you repay early."),
         ("Why is the effective rate almost twice the flat rate?", "With a flat rate you pay interest on the full original principal until the end, while the average amount you actually owe over the term is only about half.")],
    sources=[("Flat and effective (annuity) rate calculations commonly used by financing companies", "")],
)

CALC_EN["deposito"] = dict(
    short="Time Deposit Calculator", chip="Deposit",
    title="Time Deposit Calculator Indonesia 2026 – Net Interest After 20% Tax",
    h1="Time Deposit (Deposito) Interest Calculator",
    desc="Calculate net time-deposit interest after the 20% final tax, interest per period, and the final balance with automatic rollover (ARO).",
    card="Net interest after 20% tax and ARO simulation.",
    lead="Calculate the deposit interest you actually receive after tax, then simulate the balance if the deposit is rolled over automatically (ARO) several times.",
    form=money("nominal", "Deposit amount", "100000000") + num("bunga", "Interest rate per year", "4", "%")
    + sel("tenorBulan", "Term", [(1, "1 month"), (3, "3 months"), (6, "6 months"), (12, "12 months"), (24, "24 months")], 12)
    + num("perpanjang", "Number of periods", "1", "×", "How many times the deposit is rolled over (including the first period).")
    + '<div class="fld"><label>Rollover</label>' + chk("aro", "ARO + interest (interest is redeposited)", True) + "</div>",
    sections=[
        ("How deposit interest is calculated", """<div class="formula">Gross interest = Amount × annual rate × term (months) ÷ 12
Tax = 20% × gross interest (if the balance is above Rp7,500,000)
Net interest = Gross interest − Tax</div>
<p>Banks actually calculate interest by the number of days, so bank figures may differ slightly.</p>"""),
        ("Tax on deposit interest", """<p>Deposit interest is subject to a <b>20% final income tax</b> withheld directly by the bank. Interest is not taxed if your total deposits and savings at that bank do not exceed Rp7,500,000.</p>"""),
        ("How safe are deposits: LPS guarantee", """<p>Deposits at banks that participate in the Indonesia Deposit Insurance Corporation (LPS) are guaranteed up to <b>Rp2 billion per customer per bank</b>, provided the interest rate you receive does not exceed the <b>LPS guaranteed rate</b> in force. If the bank offers more than that, your deposit may not be covered. Check the latest guaranteed rate on the LPS website before placing funds.</p>"""),
        ("ARO, ARO + interest, and non-ARO", """<ul><li><b>ARO + interest</b>: principal and interest roll over automatically, so interest earns interest (compounding).</li>
<li><b>ARO principal only</b>: principal rolls over, interest is paid to your savings account.</li><li><b>Non-ARO</b>: funds return to your savings account at maturity.</li></ul>
<p>Untick ARO + interest to see the result if interest is withdrawn at each maturity.</p>"""),
    ],
    faq=[("Is a deposit better than a money market fund?", "Deposits pay a fixed rate and are guaranteed by LPS (with conditions), but the money is locked until maturity. Money market funds are more flexible and taxed differently, but returns are not guaranteed. Compare net returns after tax."),
         ("What if I withdraw before maturity?", "Banks usually charge a penalty or pay no interest for the current period. Check your bank's terms."),
         ("Do I report deposit interest in my annual tax return?", "Yes. Deposit interest is reported as income subject to final tax, and the deposit balance is reported as an asset.")],
    sources=[("Final income tax on deposit and savings interest (PP 131/2000 and amendments)", ""), ("Indonesia Deposit Insurance Corporation (LPS) – deposit guarantee rules", "")],
)

CALC_EN["investasi"] = dict(
    short="Investment Calculator", chip="Investment",
    title="Investment & Compound Interest Calculator – Monthly Investing Simulation",
    h1="Regular Investment and Compound Interest Calculator",
    desc="Simulate the value of an investment from an initial amount and regular monthly contributions with compound returns, including a year-by-year growth table.",
    card="Value of regular monthly investing with compounding.",
    lead="See how an initial amount and regular contributions grow with compound interest. Useful for planning education funds, retirement, or a house down payment.",
    form=money("awal", "Initial amount", "10000000") + money("bulanan", "Monthly contribution", "1000000") + num("imbal", "Expected annual return", "8", "%")
    + num("tahun", "Time horizon", "10", "years") + num("kenaikan", "Annual increase in contribution", "0", "%", "For example 5% a year in line with salary increases."),
    sections=[
        ("What is compound interest?", """<p>Compound interest means returns are reinvested so they also earn returns. Over the long term the effect is huge: the longer money stays invested, the larger the share of returns compared with contributions.</p>
<div class="formula">Next month's balance = Balance × (1 + i) + monthly contribution
i = (1 + annual return)^(1/12) − 1</div>"""),
        ("Choosing a realistic return", """<p>Returns are not guaranteed and vary by instrument. As a rough guide (not a promise): deposits and money market funds return a few percent a year, bonds slightly more, while stocks and equity funds can return more over the long term but swing sharply. Use several scenarios: pessimistic, moderate, and optimistic.</p>"""),
        ("Don't forget inflation", """<p>Rp100 million in 15 years is not worth the same as Rp100 million today. To see the real value, subtract expected inflation from the return (for example an 8% return and 3% inflation is about 5% real), then recalculate.</p>"""),
        ("Example", """<p>An initial Rp10,000,000 plus Rp1,000,000 a month for 10 years at 8% a year. Total contributions are Rp130,000,000; the final value is about <b>Rp201.7 million</b>, meaning about Rp71.7 million comes from investment returns.</p>"""),
    ],
    faq=[("Is this result guaranteed?", "No. It is a mathematical simulation with a fixed return; real investments go up and down and can lose money. Use it as a planning tool."),
         ("Does it include tax and fees?", "No. Enter a return net of management fees and taxes for a more realistic result."),
         ("Are contributions at the start or end of the month?", "This calculator assumes contributions at the end of each month, so results are slightly conservative.")],
    sources=[("Future value of an annuity with monthly compounding", "")],
)

PAGES_EN = {
    "tentang": ("About Us", """<p><b>{name}</b> is a set of financial calculators for people living and working in Indonesia: income tax (PPh 21), take-home pay, THR, BPJS contributions, mortgages (KPR), vehicle loans, time deposits, and investments.</p>
<p>Each calculator follows the official rules in force, such as PP 58/2023 and PMK 168/2023 for PPh 21, the HPP Law for Article 17 rates, and the latest BPJS regulations. Every page shows the formula, a worked example, and the regulatory source so you can check the results yourself.</p>
<h2>Our principles</h2><ul><li><b>Transparent</b>: calculation steps are always shown.</li><li><b>Private</b>: all calculations run on your device; the numbers you enter are not sent to a server.</li>
<li><b>Up to date</b>: rules are updated when official changes take effect, and the update date is shown on every page.</li></ul>
<h2>Who runs this site</h2><p>{name} is built by the same developers behind <a href="https://getcomput.com" target="_blank" rel="noopener">GetComput</a>, an Indonesian-language statistics learning platform.</p>
<p>Have an idea for a new calculator or found a mistake? <a href="{fb}">Send us feedback</a>.</p>"""),
    "kontak": ("Contact", """<p>We welcome suggestions, error reports, and ideas for new calculators.</p>
<p>📝 Fastest: use the <a href="{fb}">feedback form</a>. Messages go straight to our task list.</p>
<p>📧 Email: <a href="mailto:{email}">{email}</a></p>
<p>To help us respond quickly, include the calculator name, the numbers you entered, and the result you think is wrong. We cannot provide personal tax or financial consulting.</p>"""),
    "privasi": ("Privacy Policy", """<p>Last updated: {updated}.</p>
<h2>Data you enter</h2><p>All calculators run in your browser. The numbers you enter (salary, house price, and so on) are not sent to our servers and are not stored by us. If you use the “copy result link” feature, those numbers become part of the link you choose to share.</p>
<h2>Cookies, analytics, and ads</h2><p>This site may use Google Analytics to understand usage in aggregate and may show third-party ads through Google AdSense. Google and its partners may use cookies or similar identifiers to serve and measure ads, including personalized ads based on your visits to this and other sites.</p>
<p>You can manage ad personalization at <a href="https://adssettings.google.com" target="_blank" rel="noopener">adssettings.google.com</a> and learn how Google uses data at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>. Visitors from regions that require consent will see a consent message from Google.</p>
<h2>Feedback form</h2><p>If you send feedback, we store the message, the feedback type, the related page, and your name and email if provided, together with the time and country of submission. This data is stored privately, read only by the site owner to improve the site and reply to messages, and is not shared with third parties. You may request deletion by email.</p>
<h2>Contact</h2><p>Privacy questions can be sent to <a href="mailto:{email}">{email}</a>.</p>"""),
    "syarat": ("Terms of Use & Disclaimer", """<p>Last updated: {updated}.</p>
<h2>Disclaimer</h2><p>All results on {name} are <b>simulations and general information</b>, not financial, tax, investment, or legal advice. Results may differ from calculations by banks, employers, or the tax office due to different components, rounding, internal policies, or rule changes.</p>
<p>Before making important decisions, confirm with the relevant party, such as HR, your bank, a tax consultant, or a financial planner.</p>
<h2>Use</h2><p>You may use these calculators free of charge for personal and professional purposes. Mass copying of the site's content or using it to mislead others is prohibited.</p>
<h2>Ads and links</h2><p>This site is supported by advertising. Ads shown come from third parties and are not our recommendations.</p>"""),
}
