"""Additional guide sections (English). Inserted before the last (tips) section of the guide with the same Indonesian slug."""
from articles_more import T

EXTRA_EN = {}

EXTRA_EN["apa-itu-pph-21-ter"] = [
    ("Full example: Rp15 million salary, K/1 status", """<p>To make it concrete, let's calculate PPh 21 for an employee with <b>K/1</b> status (married, one child), base salary plus fixed allowances of <b>Rp15,000,000</b> a month, enrolled in all BPJS programs at very low work risk, with no bonus.</p>
<p><b>Step 1 – monthly gross.</b> On top of salary, the employer pays BPJS Health 4% (Rp480,000, because of the Rp12 million wage cap), JKK 0.24% (Rp36,000), and JKM 0.3% (Rp45,000). All three are added to gross income, so monthly gross is <b>Rp15,561,000</b>.</p>
<p><b>Step 2 – TER for January–November.</b> K/1 falls in category B. For gross income of Rp15,561,000 the TER rate is 6%, so each month <b>Rp933,660</b> is withheld. Over 11 months that totals Rp10,270,260.</p>
<p><b>Step 3 – the December calculation.</b></p>""" + T(["Component", "Annual"], [
        ["Gross income (12 × Rp15,561,000)", "Rp186,732,000"], ["− Job expense deduction (capped)", "Rp6,000,000"], ["− Employee JHT 2% and JP 1%", "Rp4,930,356"],
        ["=Net income", "Rp175,801,644"], ["− PTKP K/1", "Rp63,000,000"], ["=Taxable income (rounded to thousands)", "Rp112,801,000"],
        ["5% × Rp60,000,000", "Rp3,000,000"], ["15% × Rp52,801,000", "Rp7,920,150"], ["=Annual PPh 21", "Rp10,920,150"],
        ["− Already withheld January–November", "Rp10,270,260"], ["=December PPh 21", "Rp649,890"]]) + """
<p>December's deduction (Rp649,890) is actually smaller than a normal month. That's normal: the TER rate for this income level is slightly higher than the true annual effective rate, so December acts as the adjustment month. Total annual tax remains <b>Rp10,920,150</b>, about 5.8% of gross income.</p>"""),
    ("Common misconceptions", """<ul><li><b>&ldquo;TER is a final tax.&rdquo;</b> No. TER is only how tax is withheld each month. The actual tax is still recalculated for the year with the Article 17 rates.</li>
<li><b>&ldquo;Bonuses are taxed at a higher rate.&rdquo;</b> A bonus does make that month's deduction jump, but at year end all income is added up and taxed at the same rates. There is no special bonus rate.</li>
<li><b>&ldquo;A status change takes effect immediately.&rdquo;</b> PTKP status follows your situation at the start of the tax year. Marrying or having a child mid-year affects the next tax year.</li>
<li><b>&ldquo;If my salary is below PTKP, nothing is withheld.&rdquo;</b> In normal months the TER rate for low income is 0%. But a large bonus in one month can trigger temporary withholding, which is refunded in December.</li>
<li><b>&ldquo;Changing jobs needs no paperwork.&rdquo;</b> It is important to get the withholding slip from your old employer. Without it, the new employer calculates as if you just started working, and you may owe tax when you file your return.</li></ul>"""),
    ("Key terms to understand", """<ul><li><b>Gross income (bruto)</b>: all income before any deduction, including insurance premiums paid by the employer.</li>
<li><b>Job expense deduction (biaya jabatan)</b>: an automatic 5% deduction from gross income, up to Rp500,000 a month or Rp6,000,000 a year, to cover the cost of earning income.</li>
<li><b>Net income (neto)</b>: gross minus the job expense deduction and pension/JHT contributions paid by the employee.</li>
<li><b>PTKP</b>: the non-taxable income threshold, set by marital status and number of dependants.</li>
<li><b>PKP</b>: taxable income, which is net income minus PTKP, rounded down to the nearest thousand rupiah.</li>
<li><b>Withholding slip 1721-A1</b>: the employer's document summarizing income and tax for the year.</li>
<li><b>Underpaid / overpaid</b>: the difference between annual tax due and tax already withheld.</li></ul>"""),
]

EXTRA_EN["cara-membaca-slip-gaji"] = [
    ("A sample payslip and how to read it", """<p>Here is a normal-month payslip for an employee with TK/0 status and a Rp10,000,000 salary, enrolled in all BPJS programs (very low work risk):</p>""" + T(["Component", "Amount"], [
        ["Base salary", "Rp8,000,000"], ["Position allowance (fixed)", "Rp2,000,000"], ["=Total earnings", "Rp10,000,000"],
        ["BPJS Health 1%", "−Rp100,000"], ["JHT 2%", "−Rp200,000"], ["JP 1%", "−Rp100,000"], ["PPh 21 (TER category A 2.5% × Rp10,454,000)", "−Rp261,350"],
        ["=Net pay transferred", "Rp9,338,650"]]) + """
<p>A few things to note in this example:</p>
<ul><li>PPh 21 is calculated on <b>Rp10,454,000</b>, not Rp10,000,000, because BPJS Health (Rp400,000), JKK (Rp24,000), and JKM (Rp30,000) premiums paid by the employer count as income.</li>
<li>Employer contributions usually do <b>not</b> appear as deductions because they are not taken from your salary. Some companies list them for information.</li>
<li>Overtime, bonuses, or attendance deductions will change that month's figures.</li></ul>"""),
    ("Your right to a payslip", """<p>Under the wage regulations (PP 36/2021 and amendments), employers must provide <b>proof of wage payment</b> with a breakdown of wages every time wages are paid. It may be on paper or electronic, such as by email or an HR app.</p>
<p>A payslip is more than a formality. You need it to apply for a mortgage, vehicle loan, credit card, visa, or scholarship, and it serves as evidence in a wage dispute. Keep your payslips at least while you work at the company and for a few years afterwards.</p>"""),
    ("Common payslip mistakes", """<ul><li><b>Wrong PTKP status</b>, such as being married but still recorded as TK/0, so more tax is withheld.</li>
<li><b>BPJS contribution base too low</b>, for example using only base salary when there are fixed allowances. Your JHT balance and pension end up smaller.</li>
<li><b>Overtime not calculated by the rules</b>, such as a flat hourly rate without the 1.5× and 2× multipliers.</li>
<li><b>Unexplained deductions</b>, such as vague &ldquo;other deductions&rdquo;.</li>
<li><b>Missed back pay</b> after a minimum wage adjustment or promotion.</li></ul>
<p>If something looks wrong, ask HR politely and bring your own calculation. Most errors come from outdated data rather than bad intent.</p>"""),
]

EXTRA_EN["aturan-thr-dan-tips-mengelolanya"] = [
    ("Worked examples for different situations", """<p>Some examples to make the pro-rata rule easier to understand:</p>""" + T(["Situation", "Calculation", "THR"], [
        ["Permanent employee, 3 years, wages Rp7,000,000", "1 × Rp7,000,000", "Rp7,000,000"],
        ["Contract employee, 4 months, wages Rp6,000,000", "4/12 × Rp6,000,000", "Rp2,000,000"],
        ["New employee, 1 month, wages Rp9,000,000", "1/12 × Rp9,000,000", "Rp750,000"],
        ["Daily worker, 8 months, average wages Rp3,600,000", "average monthly wage over the period worked", "Rp3,600,000 × 8/12 = Rp2,400,000"],
        ["New employee, 3 weeks", "less than 1 month", "not yet entitled"]]) + """
<p>Length of service is counted up to the employee's religious holiday, not the THR payment date. If the company's THR policy is more generous than the rules, the more favorable policy applies.</p>"""),
    ("What about freelancers and app-based partners?", """<p>Regulation 6/2016 covers the employment relationship between <b>employers and employees</b>. Project-based freelancers without an employment relationship, and app-based drivers with partnership status, are generally not covered by those THR rules. The government has urged app companies to give holiday bonuses to their partners, but the form and amount follow each company's policy.</p>
<p>If you work as a partner or freelancer, consider building your own &ldquo;THR&rdquo; by setting aside part of your income each month, for example 8–10%, in a separate account. Over a year it adds up to roughly one month's income.</p>"""),
    ("Common mistakes when receiving THR", """<ul><li><b>Spending THR before it arrives</b>, for example with credit cards or paylater early in Ramadan.</li>
<li><b>Forgetting the tax</b>, so the budget is based on gross THR.</li>
<li><b>Spending it all on consumption</b>, leaving nothing for savings or post-holiday needs.</li>
<li><b>Social pressure</b>, such as buying new things or giving gifts beyond your means.</li>
<li><b>Borrowing to travel home</b>, then struggling with installments for months.</li></ul>
<p>A simple approach is to split net THR into fixed buckets, for example 40% holiday needs, 20% giving, 20% travel and visits, and 20% savings. Adjust the percentages to your family's situation.</p>"""),
]

EXTRA_EN["mengenal-bpjs-kesehatan-dan-ketenagakerjaan"] = [
    ("Illustration: how much builds up in JHT?", """<p>An employee earning <b>Rp8,000,000</b> contributes 5.7% to JHT each month (3.7% from the employer and 2% from the employee), which is <b>Rp456,000</b>. That adds up to Rp5,472,000 a year and about <b>Rp54.7 million</b> over 10 years from contributions alone, before investment returns credited by BPJS Employment and salary increases.</p>
<p>That is why JHT shouldn't be withdrawn every time you change jobs. If the balance is left to grow and merged into your membership at the next employer, JHT can become a meaningful retirement fund alongside the pension (JP).</p>"""),
    ("Self-paying members and non-salaried workers", """<p>Not everyone is an employee. For them there are different schemes:</p>
<ul><li><b>Self-paying BPJS Health</b>: you pay a fixed amount per person per month based on class, for each registered family member. Amounts follow the applicable presidential regulation.</li>
<li><b>BPJS Employment for non-wage earners (BPU)</b>: suitable for traders, freelancers, online drivers, farmers, and other self-employed workers. The basic programs are JKK and JKM, with contributions based on declared income, starting from the tens of thousands of rupiah a month. JHT can be added optionally.</li></ul>
<p>For self-employed people, JKK coverage is very valuable: treatment after a work accident can be extremely expensive, while the contribution is small.</p>"""),
    ("Common BPJS mistakes", """<ul><li><b>Falling behind on self-paid BPJS Health.</b> Membership can become inactive, and reactivation may carry penalties for certain inpatient services.</li>
<li><b>Not updating family data</b> after marrying or having a child, so family members aren't covered.</li>
<li><b>Assuming BPJS Employment moves automatically</b> when you change jobs. Make sure the new employer continues your membership with the same number.</li>
<li><b>Not reporting a work accident</b> within the deadline, delaying the JKK claim.</li>
<li><b>Ignoring JP</b> because its benefits come only in retirement. The minimum 15-year contribution period decides whether you receive a monthly pension.</li></ul>"""),
]

EXTRA_EN["panduan-kpr-rumah-pertama"] = [
    ("A worked KPR example", """<p>A <b>Rp600 million</b> house with a 20% down payment (Rp120 million) means a loan of <b>Rp480 million</b>. Term 15 years, 4.5% fixed for 3 years, then 11% floating.</p>""" + T(["Period", "Monthly installment", "Notes"], [
        ["Years 1–3 (4.5% fixed)", "Rp3,671,968", "Year 1: interest Rp21.1 million, principal Rp22.9 million"],
        ["Years 4–15 (11% floating)", "Rp5,114,414", "Recalculated on remaining principal of about Rp408 million"],
        ["=Total interest over 15 years", "about Rp388.7 million", "Almost 81% of the loan amount"]]) + """
<p>Notice two things. First, in year one almost half of each installment goes to interest. Second, after 3 years about Rp408 million is still owed, meaning only about 15% of the principal has been repaid, while the installment rises by about Rp1.44 million a month. For a Rp5.1 million installment, banks typically require income of around Rp17 million a month.</p>"""),
    ("Conventional vs. sharia KPR", T(["Aspect", "Conventional", "Sharia (murabahah)"], [
        ["Basis", "Loan with interest", "Sale with a profit margin"],
        ["Installments", "Fixed for some years, then floating", "Usually fixed until paid off"],
        ["Risk of higher installments", "Yes, when floating rates rise", "None for fixed-margin contracts"],
        ["Total cost", "Can be lower if rates fall", "Known upfront, sometimes higher"],
        ["Early repayment", "Penalty per bank terms", "Per contract and bank terms"]]) + """
<p>A fixed-margin sharia KPR gives certainty, suitable if you don't want interest-rate risk. A conventional KPR can be attractive if you expect rates to fall or plan to repay early. Compare the total payment of both, not just the first month's installment.</p>"""),
    ("The KPR process from start to signing", """<ol><li><b>Work out what you can afford</b>: maximum installment (30–35% of income) and available upfront cash.</li>
<li><b>Find a house</b> and check its legal status: certificate, building permit (IMB/PBG), and the developer's reputation.</li>
<li><b>Apply to several banks</b> with complete documents. Banks check SLIK OJK and repayment capacity.</li>
<li><b>Appraisal</b>: the bank values the house. The loan limit may be lower than the price if the valuation is lower.</li>
<li><b>Credit approval letter (SP3K)</b>: states the limit, rate, term, and fees. Read it carefully.</li>
<li><b>Signing before a notary</b>: the loan agreement, sale deed (AJB), and mortgage deed (APHT), plus payment of fees.</li>
<li><b>Disbursement and handover</b>: funds go to the seller or developer, and you receive the keys.</li></ol>
<p>The process can take weeks to months depending on document completeness and whether the house is ready or still under construction.</p>"""),
]

EXTRA_EN["bunga-flat-vs-efektif-kredit-kendaraan"] = [
    ("Example: comparing two offers", """<p>You want a <b>Rp25 million</b> motorcycle with a 20% down payment, so the loan is Rp20 million over 36 months. Two offers:</p>""" + T(["", "Offer A", "Offer B"], [
        ["Advertised rate", "5% flat per year", "9% effective per year"], ["Monthly installment", "Rp638,889", "Rp635,995"],
        ["Total interest over 36 months", "Rp3,000,000", "Rp2,895,808"], ["=Equivalent effective rate", "about 9.3%", "9%"]]) + """
<p>At first glance Offer A looks much cheaper because it says &ldquo;5%&rdquo;. Converted to the same basis, Offer B is actually slightly cheaper. That's why comparing a flat rate directly with an effective rate can be misleading.</p>"""),
    ("Reading leasing brochures and simulations", """<ul><li><b>Look for the total payment</b>, not just the installment. Multiply the installment by the number of months, then add the down payment and upfront fees.</li>
<li><b>Be careful with &ldquo;low down payment&rdquo;</b>. A small down payment means a large loan and more total interest.</li>
<li><b>Check whether insurance is included</b> in the installment, and which type (comprehensive or total loss only).</li>
<li><b>Ask about the first installment</b>: paid upfront with the down payment or the following month.</li>
<li><b>Be wary of &ldquo;0% interest&rdquo; promotions</b>. The cost is sometimes moved into the vehicle price, admin fees, or insurance. Compare with the cash price.</li></ul>"""),
    ("Borrow now or save and pay cash?", """<p>A loan lets you use the vehicle now, at the cost of interest. Saving first is cheaper but takes time and discipline. Consider:</p>
<ul><li><b>If the vehicle earns money</b> (for business, ride-hailing, or commuting that replaces large transport costs), a loan can make sense as long as installments are safe.</li>
<li><b>If the vehicle is a lifestyle purchase</b>, saving and paying cash or with a large down payment is usually wiser.</li>
<li><b>Vehicles lose value.</b> After 3 years the resale value can be far below what you paid in total.</li></ul>
<p>A middle path: save the largest down payment you can, choose the shortest comfortable term, and keep your emergency fund intact.</p>"""),
]

EXTRA_EN["panduan-deposito-untuk-pemula"] = [
    ("An ARO deposit example", """<p>A <b>Rp100 million</b> deposit at 4% a year, 12-month term, automatically rolled over with interest (ARO + interest) for three periods:</p>""" + T(["Period", "Net interest (after 20% tax)", "Balance at end of period"], [
        ["1", "Rp3,200,000", "Rp103,200,000"], ["2", "Rp3,302,400", "Rp106,502,400"], ["3", "Rp3,408,077", "Rp109,910,477"]]) + """
<p>Net interest grows each period because previous interest is redeposited. The net return is about 3.2% a year. Assuming rates stay the same, the balance grows by almost Rp10 million in three years with no extra deposits.</p>
<p>In reality, the rate at rollover follows the rate in force at that time, so it can go up or down.</p>"""),
    ("Deposits, regular savings, and planned savings", T(["", "Regular savings", "Planned savings", "Time deposit"], [
        ["Purpose", "Daily transactions", "Regular saving toward a goal", "Parking money you don't need yet"],
        ["Deposits", "Anytime", "Monthly, by auto-debit", "Once at the start"],
        ["Withdrawals", "Anytime", "At maturity", "At maturity"],
        ["Interest", "Lowest", "Higher than regular savings", "Usually the highest of the three"],
        ["Good for", "Daily money and part of the emergency fund", "Building a saving habit", "Money already accumulated"]]) + """
<p>All three complement each other: regular savings for daily needs, planned savings to build up funds gradually, and deposits to hold accumulated funds at a higher rate.</p>"""),
    ("The deposit ladder strategy", """<p>Laddering means splitting money into several deposits with different maturities. For example, Rp60 million split into:</p>
<ul><li>Rp20 million for 3 months,</li><li>Rp20 million for 6 months,</li><li>Rp20 million for 12 months.</li></ul>
<p>Whenever one matures, you can use it if needed or roll it into the longest term. Part of your money is always available soon, while the rest earns longer-term rates. The strategy also reduces the risk of bad timing when rates change.</p>"""),
]

EXTRA_EN["bunga-majemuk-dan-investasi-rutin"] = [
    ("The power of starting early", """<p>Compare two people who both want a fund at age 55, assuming an 8% annual return:</p>""" + T(["", "Rina", "Budi"], [
        ["Starts investing", "Age 25", "Age 35"], ["Monthly contribution", "Rp1,000,000", "Rp2,000,000"],
        ["Years invested", "30 years", "20 years"], ["Total contributions", "Rp360 million", "Rp480 million"], ["=Value at 55", "about Rp1.41 billion", "about Rp1.14 billion"]]) + """
<p>Budi contributes twice as much each month and Rp120 million more in total, yet still ends up behind Rina. Ten extra years give compounding time to work. The message is simple: start now, even with a small amount.</p>"""),
    ("Know your risk profile", """<p>Before choosing instruments, understand how big a drop you can handle without panicking:</p>
<ul><li><b>Conservative</b>: uncomfortable seeing values fall. Focus on money market funds, deposits, and government bonds.</li>
<li><b>Moderate</b>: can accept moderate swings for better returns. A mix of bonds, balanced funds, and some stocks.</li>
<li><b>Aggressive</b>: ready for large short-term drops for higher long-term potential. A larger share in stocks.</li></ul>
<p>Your time horizon matters too. Money needed next year shouldn't be in stocks even if you are aggressive. Licensed investment platforms usually ask you to complete a risk profile questionnaire before buying.</p>"""),
    ("Common beginner mistakes", """<ul><li><b>Following the crowd</b> into trending products without understanding them.</li>
<li><b>Expecting to get rich quickly</b> and switching products every time there is a dip.</li>
<li><b>No emergency fund</b>, forcing you to sell investments when prices are down.</li>
<li><b>Putting everything into one product</b> or one stock.</li>
<li><b>Ignoring fees</b> for buying, selling, and management that eat into returns.</li>
<li><b>Falling for guaranteed high returns</b> from parties not registered with OJK.</li></ul>"""),
]

EXTRA_EN["cara-lapor-spt-tahunan-karyawan"] = [
    ("Filling in assets and debts", """<p>The assets and debts section often causes confusion. Some simple guidelines:</p>
<ul><li><b>Cash and equivalents</b>: savings, current accounts, and deposits as of 31 December.</li>
<li><b>Vehicles and property</b>: recorded at <b>acquisition cost</b> (purchase price), with no need to revalue each year.</li>
<li><b>Investments</b>: mutual funds, stocks, bonds, and gold at acquisition value or as instructed in the filing guide.</li>
<li><b>Debts</b>: remaining principal of mortgages, vehicle loans, credit cards, and other loans as of 31 December.</li></ul>
<p>Assets bought on credit are still recorded at acquisition cost, with the remaining loan recorded under debts. Make sure year-to-year changes in assets make sense relative to your income.</p>"""),
    ("If you have other income", """<ul><li><b>Deposit interest, SBN coupons, and certain prizes</b> are already subject to final tax. Just report them; they are not recalculated.</li>
<li><b>A side business</b> with turnover up to Rp4.8 billion a year may use the 0.5% final rate on turnover under PP 55/2022 (for a limited period). Individuals with turnover up to Rp500 million a year are not taxed on that portion of turnover.</li>
<li><b>Freelance fees</b> not withheld by the payer must be added to salary and may lead to underpayment.</li>
<li><b>Income from two employers</b> in a year almost always leads to underpayment, because each employer applies PTKP and the lower brackets.</li></ul>"""),
    ("If you made a mistake after filing", """<p>Mistakes can be fixed with an <b>amended return (SPT pembetulan)</b>. In Coretax, choose the <b>Pembetulan</b> model when creating the draft, then change the incorrect parts. Amendments can be made as long as the tax office has not started an audit.</p>
<p>If the amendment results in underpayment, pay the shortfall; interest penalties may apply under the rules. If it results in overpayment, you can request a refund. It is better to correct it yourself than wait for a notice.</p>"""),
]

EXTRA_EN["cara-menghitung-upah-lembur"] = [
    ("Example: overtime on working days", """<p>Wage Rp6,000,000 a month, hourly wage Rp34,682. In one month the employee works overtime on 5 working days, 3 hours each.</p>""" + T(["Item", "Calculation", "Amount"], [
        ["First hour", "1.5 × Rp34,682", "Rp52,023"], ["Second and third hours", "2 × 2 × Rp34,682", "Rp138,728"],
        ["=Overtime pay per day", "", "Rp190,751"], ["=Overtime pay per month", "5 × Rp190,751", "Rp953,757"]]) + """
<p>Total monthly overtime is almost Rp1 million, about 16% of wages. That's large enough to check on your payslip every month.</p>"""),
    ("Overtime, tax, and BPJS", """<ul><li><b>Tax</b>: overtime pay is variable income added to that month's salary for PPh 21 under the TER method. Large overtime can push that month's TER rate up a bracket.</li>
<li><b>BPJS</b>: contributions are based on fixed wages (base salary and fixed allowances). Overtime does not increase BPJS contributions.</li>
<li><b>THR and severance</b>: also based on fixed wages, so overtime pay is not included.</li></ul>"""),
    ("Other overtime rights", """<p>Besides pay, employees working overtime are entitled to adequate rest. For overtime of 4 hours or more, the employer must provide food and drink of at least 1,400 calories, and this may not be replaced with cash. Companies must also keep a record of who worked overtime and for how long.</p>
<p>If you regularly work far beyond 4 hours a day or 18 hours a week, it's a sign your workload needs discussing. Beyond pay, prolonged fatigue is a health and safety risk.</p>"""),
]

EXTRA_EN["tips-negosiasi-gaji"] = [
    ("Setting the number you'll ask for", """<p>Say your current salary is Rp8,000,000 gross and market research shows the new role pays Rp9–12 million. To build your numbers:</p>
<ol><li><b>Minimum</b>: the salary at which moving is still worth it after commuting, travel time, and lost benefits. For example Rp9.5 million.</li>
<li><b>Reasonable</b>: the market midpoint that fits your experience, for example Rp10.5 million.</li>
<li><b>Opening</b>: slightly above reasonable to leave room, for example Rp11–12 million.</li></ol>
<p>Raises when switching jobs are often larger than annual raises at the same company, but they must be backed by strong reasons: skills, achievements, and bigger responsibilities.</p>"""),
    ("Negotiation mistakes", """<ul><li><b>Naming a number too early</b>, before understanding the scope and benefits.</li>
<li><b>Not distinguishing gross and net</b>, then agreeing to a number smaller than expected.</li>
<li><b>Lying about your current salary</b>. It can surface through payslips or tax withholding slips.</li>
<li><b>Ultimatums</b> or aggressively playing offers against each other.</li>
<li><b>Accepting on the spot</b> without asking for time to consider. Asking for a day or two is perfectly normal.</li></ul>"""),
    ("Asking for a raise at your current company", """<p>Negotiation isn't only for new jobs. To ask for a raise where you are:</p>
<ul><li><b>Choose the right moment</b>, such as before a performance review or after finishing an important project.</li>
<li><b>Prepare evidence</b>: measurable achievements, additional responsibilities, and market data.</li>
<li><b>Ask professionally</b> in a dedicated meeting, not in passing.</li>
<li><b>Have alternatives</b>: if there's no budget yet, ask for a review date, training, or a clear promotion path.</li></ul>"""),
]

EXTRA_EN["cara-membuat-anggaran-50-30-20"] = [
    ("Budget examples for two situations", """<p><b>Single in a big city, net salary Rp6,000,000:</b></p>""" + T(["Bucket", "Share", "Amount", "Examples"], [
        ["Needs", "55%", "Rp3,300,000", "Rented room Rp1.8M, food Rp1M, transport and phone Rp500K"],
        ["Wants", "25%", "Rp1,500,000", "Going out, entertainment, shopping"],
        ["Savings & investing", "20%", "Rp1,200,000", "Emergency fund first, then mutual funds"]]) + """
<p><b>Family with one child, combined net salary Rp12,000,000:</b></p>""" + T(["Bucket", "Share", "Amount", "Examples"], [
        ["Needs", "55%", "Rp6,600,000", "Mortgage, groceries, school, electricity, transport"],
        ["Wants", "20%", "Rp2,400,000", "Eating out, holidays, hobbies"],
        ["Savings & investing", "25%", "Rp3,000,000", "Emergency fund, education fund, retirement"]]) + """
<p>Neither example is exactly 50/30/20, and that's fine. What matters is that savings come first and spending doesn't exceed income.</p>"""),
    ("Other methods to try", """<ul><li><b>Zero-based budgeting</b>: every rupiah of income gets a job until nothing is left. More detailed, good for people who like tracking.</li>
<li><b>Envelope method</b>: money is split into physical or digital &ldquo;envelopes&rdquo; per category. When an envelope is empty, that category stops for the month.</li>
<li><b>Pay yourself first</b>: only set the savings percentage upfront and spend the rest freely. Simplest for beginners.</li></ul>
<p>Choose the method you are most likely to stick with. A simple budget you follow beats a perfect budget you abandon.</p>"""),
    ("Plugging budget leaks", """<p>Leaks usually come from small, frequent spending: coffee, delivery fees, forgotten app subscriptions, admin fees, or impulse buys with paylater. To fix them:</p>
<ul><li>Review last month's bank and e-wallet statements and mark unplanned spending.</li>
<li>Cancel subscriptions you rarely use.</li><li>Apply a 24-hour wait before unplanned purchases.</li>
<li>Turn off paylater if it often leads to overspending.</li></ul>"""),
]

EXTRA_EN["cara-cek-saldo-dan-klaim-jht"] = [
    ("Illustration of JHT balance growth", """<p>JHT contributions are 5.7% of wages each month. For several wage levels, accumulated contributions (before investment returns) are:</p>""" + T(["Monthly wage", "Monthly JHT", "5 years", "10 years"], [
        ["Rp5,000,000", "Rp285,000", "Rp17.1 million", "Rp34.2 million"], ["Rp8,000,000", "Rp456,000", "Rp27.4 million", "Rp54.7 million"],
        ["Rp12,000,000", "Rp684,000", "Rp41.0 million", "Rp82.1 million"]]) + """
<p>Actual balances are usually higher thanks to annual investment returns and wage increases over time. You can see the full history in the JMO app.</p>"""),
    ("JHT, JP, and JKP when you stop working", T(["Program", "When you stop working", "Form of benefit"], [
        ["JHT", "Balance can be withdrawn after the waiting period", "Lump-sum cash"],
        ["JP", "If contributions are under 15 years, contributions plus returns are paid as a lump sum at retirement age; otherwise a monthly pension", "Monthly or lump sum depending on eligibility"],
        ["JKP", "If laid off and membership requirements are met", "Cash for several months, labor-market information, training"]]) + """
<p>JKP is only for employees who are laid off, not those who resign, and requires a minimum contribution period. If you are laid off, apply for JKP within the deadline, because its benefits differ from JHT.</p>"""),
    ("Problems that often delay claims", """<ul><li><b>Data mismatches</b> between your ID card, BPJS records, and bank account, such as name spelling or date of birth.</li>
<li><b>Duplicate memberships</b>: more than one number from different employers. Merge balances first.</li>
<li><b>The employer hasn't reported</b> that you left, so your status is still active.</li>
<li><b>Unpaid contributions</b> at a previous employer, so the balance is lower than expected.</li>
<li><b>Unclear documents</b> when uploading, such as blurry photos.</li></ul>
<p>Most of these can be resolved by contacting a branch office or official BPJS Employment customer service.</p>"""),
]

EXTRA_EN["pinjaman-online-vs-kredit-bank"] = [
    ("Calculating the real cost of a loan", """<p>Example: an online loan of Rp2,000,000 for 30 days at 0.2% per day with a Rp100,000 service fee deducted upfront:</p>""" + T(["Item", "Amount"], [
        ["Money you receive", "Rp1,900,000"], ["Interest 0.2% × 30 days × Rp2,000,000", "Rp120,000"], ["Amount to repay", "Rp2,120,000"],
        ["=Total cost to receive Rp1.9 million", "Rp220,000 (about 11.6% in one month)"]]) + """
<p>The upfront service fee makes the real cost much higher than the advertised rate. If you pay late, daily penalties add to the burden. That's why online loans should only be used for urgent needs when you are sure you can repay on time.</p>"""),
    ("Alternatives before borrowing", """<ul><li><b>Your emergency fund</b>; that's what it's for.</li><li><b>Selling things you don't use.</b></li>
<li><b>A salary advance</b> from your employer or staff cooperative, usually interest-free or low-interest.</li>
<li><b>Negotiating a payment schedule</b> with whoever is billing you, such as a school or hospital.</li>
<li><b>Borrowing from family</b> with a clear written agreement.</li>
<li><b>A bank personal loan or credit card</b> if you have access and can repay on schedule.</li></ul>"""),
    ("When debts pile up", """<p>If you have several debts at once, make a repayment plan:</p>
<ol><li><b>List all debts</b>: remaining principal, interest, installment, and due date.</li>
<li><b>Stop new borrowing</b>, including borrowing to repay other loans.</li>
<li><b>Choose an order</b>: the <i>avalanche</i> method (highest interest first) saves the most money; the <i>snowball</i> method (smallest balance first) builds motivation with quick wins.</li>
<li><b>Pay the minimum on every debt</b> to avoid penalties, then put extra money toward the priority debt.</li>
<li><b>Request restructuring</b> from licensed lenders if you genuinely can't pay, before falling far behind.</li></ol>"""),
]

EXTRA_EN["take-over-dan-pelunasan-kpr"] = [
    ("Example: break-even point for a take over", """<p>Continuing the example above: the take over saves about <b>Rp684,000 a month</b>. Suppose total take-over costs (penalty, provision, appraisal, notary, insurance) are about <b>Rp15,000,000</b>.</p>
<div class="formula">Break-even = Take-over cost ÷ monthly saving
           = Rp15,000,000 ÷ Rp684,000 ≈ 22 months</div>
<p>So the take over only pays off if you keep the KPR for more than about 22 months and the new bank's rate really is lower during that time. Remember that the new bank's promotional rate usually lasts only a few years before switching to floating.</p>"""),
    ("Partial prepayment: lower the installment or shorten the term?", """<p>Remaining principal Rp400 million, 11% rate, 12 years left, installment Rp5,014,221. You prepay <b>Rp50 million</b>:</p>""" + T(["Option", "Installment", "Duration", "Remaining total interest"], [
        ["No prepayment", "Rp5,014,221", "144 months", "about Rp322.0 million"],
        ["Lower installment, same term", "Rp4,387,443", "144 months", "about Rp281.8 million"],
        ["Same installment, shorter term", "Rp5,014,221", "112 months", "about Rp211.6 million"]]) + """
<p>Shortening the term saves about Rp110 million in interest, far more than lowering the installment (about Rp40 million). Choose the lower installment only if you genuinely need more monthly cash flow.</p>"""),
    ("Steps in a take over", """<ol><li>Ask your current bank for a <b>statement of the remaining loan</b> and the penalty terms.</li>
<li>Apply to the new bank with personal, income, and existing KPR documents.</li>
<li>The new bank does an <b>appraisal</b> and checks your credit history.</li>
<li>If approved, the new bank <b>pays off</b> the old loan.</li>
<li>The certificate is collected from the old bank, the old mortgage is released (<b>roya</b>), and a new mortgage is registered for the new bank.</li>
<li>You start paying installments to the new bank.</li></ol>"""),
]

EXTRA_EN["mengenal-sbn-ritel"] = [
    ("Example coupon calculation", """<p>Suppose you buy <b>Rp10,000,000</b> of retail SBN with a fixed 6% annual coupon paid monthly (the coupon is just an example; each series has its own):</p>""" + T(["Item", "Amount"], [
        ["Gross annual coupon (6% × Rp10 million)", "Rp600,000"], ["10% final tax", "Rp60,000"], ["=Net annual coupon", "Rp540,000"], ["=Net monthly coupon", "Rp45,000"]]) + """
<p>Compare with a deposit at 6% a year: after 20% tax, the net return is Rp480,000 a year. At the same rate, SBN pays more net because the tax rate is lower. The Rp10 million principal is returned in full at maturity.</p>"""),
    ("Retail SBN, deposits, and mutual funds", T(["Aspect", "Retail SBN", "Time deposit", "Money market fund"], [
        ["Guarantor", "The state", "LPS (with conditions)", "Not guaranteed"], ["Tax on returns", "10% final", "20% final", "Not taxable for the investor"],
        ["Withdrawal", "Depends on series type", "At maturity", "Any exchange day"], ["Minimum", "Usually Rp1 million", "Varies", "Can be very small"],
        ["Good for", "Goals in 2–6 years", "Fixed short-term goals", "Emergency fund and short term"]])),
    ("How to buy retail SBN", """<ol><li><b>Choose an official distribution partner</b> (bank, broker, or investment platform) listed on the Ministry of Finance website.</li>
<li><b>Register and verify</b> your identity, including a cash account and a securities account.</li>
<li><b>Watch the offering schedule</b> for the series you want, including coupon and tenor.</li>
<li><b>Order during the offering period</b>, then pay with the billing code before the deadline.</li>
<li><b>Keep proof of ownership</b>. Coupons will be paid to your account on schedule.</li></ol>"""),
]

EXTRA_EN["reksa-dana-vs-deposito"] = [
    ("Illustration: Rp10 million for one year", """<p>A simple picture of keeping Rp10 million for one year. Mutual fund figures are illustrations only, not promised returns:</p>""" + T(["Option", "Assumption", "Estimated net result"], [
        ["Time deposit", "4% a year, 20% tax", "Rp320,000, certain"],
        ["Money market fund", "4–5% a year", "Rp400,000–Rp500,000, may vary"],
        ["Equity fund", "Could be −15% to +20% in a year", "−Rp1.5 million to +Rp2 million"]]) + """
<p>Over one year, an equity fund is too risky because it may be down just when you need the money. Over five years or more, the chance that equity funds deliver higher returns grows, though it is still not guaranteed.</p>"""),
    ("How to read a fund fact sheet", """<p>A <b>fund fact sheet</b> is a fund's monthly summary. Things to check:</p>
<ul><li><b>Investment policy</b>: asset allocation, such as the percentage in stocks and bonds.</li>
<li><b>Performance</b>: 1-month, 1-year, 3-year, and since-inception returns, compared with a benchmark.</li>
<li><b>Assets under management</b>: very small funds risk being dissolved.</li>
<li><b>Fees</b>: subscription, redemption, switching, and annual management fees.</li>
<li><b>Custodian bank</b> and <b>investment manager</b>: make sure they are registered with and supervised by OJK.</li>
<li><b>Risk classification</b>: low, medium, or high.</li></ul>"""),
    ("Beginner mistakes when choosing", """<ul><li><b>Choosing based only on last month's performance</b>; past performance doesn't guarantee future results.</li>
<li><b>Selling an equity fund in a panic</b> when it falls, locking in the loss.</li>
<li><b>Keeping short-term money in equity funds</b>.</li>
<li><b>Assuming mutual funds are LPS-guaranteed</b> like deposits.</li>
<li><b>Buying through apps not registered</b> with OJK.</li></ul>"""),
]

EXTRA_EN["berapa-dana-darurat-yang-ideal"] = [
    ("Example: calculating essential expenses", """<p>An emergency fund is based on expenses you <b>must still pay</b> even if income stops. Example for a small family:</p>""" + T(["Essential expense", "Per month"], [
        ["Rent or mortgage", "Rp2,000,000"], ["Food and groceries", "Rp2,500,000"], ["Electricity, water, internet, phone", "Rp700,000"],
        ["Transport", "Rp600,000"], ["Children's school", "Rp800,000"], ["Minimum debt payments and insurance", "Rp900,000"], ["=Total essential expenses", "Rp7,500,000"]]) + """
<p>For a married couple with one child, the target is about 6–9 times that, or <b>Rp45–67.5 million</b>. Entertainment, holidays, and shopping don't need to be counted, because they can be paused in an emergency.</p>"""),
    ("When should you use it?", """<p>Ask three questions before using your emergency fund:</p>
<ul><li><b>Is it unexpected?</b> Annual school fees or vehicle tax can be planned, so they aren't emergencies.</li>
<li><b>Is it essential?</b> Health, housing, and lost income are essential. A new gadget isn't.</li>
<li><b>Is it urgent?</b> If it can wait and be saved for over a few months, don't use the emergency fund.</li></ul>
<p>If all three answers are &ldquo;yes&rdquo;, use it without hesitation; that's what it's for. Afterwards, make refilling it a priority.</p>"""),
    ("Emergency fund, insurance, and investing", T(["", "Emergency fund", "Insurance", "Investing"], [
        ["Purpose", "Cover urgent short-term needs", "Transfer big risks to an insurer", "Grow money for long-term goals"],
        ["Example risks", "Job loss, sudden repairs", "Serious illness, accident, death", "–"],
        ["Availability", "Anytime", "When a claim is approved", "May be down in value"],
        ["Order", "First", "Alongside or after a starter emergency fund", "Once the first two are adequate"]]) + """
<p>They complement each other. The emergency fund protects you from small to medium events, insurance from major ones, and investing builds your future.</p>"""),
]

CLOSE_EN = {
    "apa-itu-pph-21-ter": ("""<p>PPh 21 under the TER method only changes how tax is withheld each month, not how much tax you owe for the year. January to November use a simple rate based on monthly gross income, and December is the adjustment month using the Article 17 rates. Once you understand gross income, PTKP, the job expense deduction, and the TER categories, you can check whether your payslip deductions look right, plan for bonus months, and avoid surprises when December's payslip looks different.</p>""",
        [("Are meal and transport allowances included in TER?", "Yes, if paid in cash. All income for the month is added up as gross income and multiplied by the TER rate."),
         ("Do contract employees use TER too?", "Permanent employees and non-permanent employees paid monthly use the monthly TER. Non-permanent employees paid daily or weekly use the daily TER with separate rules.")]),
    "cara-membaca-slip-gaji": ("""<p>Your payslip is a monthly summary of your financial relationship with your employer. By understanding the difference between base salary, fixed and variable allowances, and BPJS and PPh 21 deductions, you can make sure you get what you're owed and budget from the amount you actually receive. Make a habit of checking your payslip every month and filing it neatly.</p>""",
        [("Why did my net pay change when my base salary didn't?", "It can be overtime, variable allowances, attendance deductions, BPJS changes, or a different TER rate because that month's gross income changed."),
         ("Can my employer make deductions without my consent?", "Deductions beyond legal obligations such as tax and BPJS generally need a basis in the employment agreement, company regulations, or the employee's written consent.")]),
    "aturan-thr-dan-tips-mengelolanya": ("""<p>THR is a right with clear rules: at least one month's wages for 12 months or more of service, pro-rata for shorter service, paid no later than seven days before the holiday. Because the tax deduction can spike, plan from net THR. With a clear split between holiday needs, giving, and savings, THR can bring joy without leaving a burden after the holiday.</p>""",
        [("Can THR be paid in goods?", "THR must be paid in rupiah. Gifts such as hampers do not replace the THR obligation."),
         ("Is THR calculated on wages after BPJS deductions?", "No. THR is based on one month's wages, meaning base salary plus fixed allowances, before any deductions.")]),
    "mengenal-bpjs-kesehatan-dan-ketenagakerjaan": ("""<p>BPJS contributions deducted from your salary are more than a cost. Behind them are health coverage for your family, old-age savings, a monthly pension, work-accident protection, death benefits, and support if you lose your job. Make sure your membership is active, family data is complete, and your reported wage is correct, so you can actually use these benefits when you need them.</p>""",
        [("Does a working child stay on the parents' BPJS Health?", "No. A working child is registered by their own employer. Dependent children are also limited by age and unmarried status."),
         ("What if my employer hasn't registered me with BPJS?", "Employers are required to register their employees. You can report it to BPJS or the local manpower office.")]),
    "panduan-kpr-rumah-pertama": ("""<p>A KPR makes a first home affordable sooner, but it is a financial commitment of ten to twenty-plus years. The key is preparation: a sufficient down payment, installments that stay safe if floating rates rise, upfront costs already budgeted, and a clean credit history. Simulate several scenarios before choosing a house, so your decision is based on numbers rather than promotions.</p>""",
        [("Can freelancers apply for a KPR?", "Yes, with proof of income such as bank statements for recent months or years, contracts, and tax reports. Requirements are usually stricter than for employees."),
         ("Can a couple combine incomes?", "Usually yes (joint income), so the approved limit can be higher. Both partners' credit histories will be checked.")]),
    "bunga-flat-vs-efektif-kredit-kendaraan": ("""<p>Flat and effective rates are two ways of stating the cost of a loan that can't be compared directly. Always convert to the effective rate, calculate the total payment, and include other costs such as insurance and admin fees. That way you can choose the genuinely cheapest offer and keep vehicle installments healthy for your household finances.</p>""",
        [("Is a flat rate always more expensive?", "Not always. What matters is the equivalent effective rate. A low flat rate can equal a competitive effective rate."),
         ("Can a vehicle loan rate change midway?", "With flat-rate loans the installment usually stays the same until paid off. Read the agreement to make sure there is no rate adjustment clause.")]),
    "panduan-deposito-untuk-pemula": ("""<p>Time deposits suit money with a clear purpose and timeline, offering a fixed rate and low risk. The net return is affected by the 20% tax and inflation, while safety depends on meeting the LPS guarantee conditions. Choose the right bank, match the term to your needs, and consider a ladder so your money stays within reach.</p>""",
        [("Can deposit interest be paid monthly?", "Yes. Some banks offer monthly interest payments to a savings account, especially for longer terms."),
         ("Are deposits at digital banks safe?", "Yes, if the bank is licensed by OJK, participates in LPS, and your rate does not exceed the LPS guaranteed rate.")]),
    "bunga-majemuk-dan-investasi-rutin": ("""<p>Compound interest works best with time. Start as early as you can, invest regularly, raise contributions as income grows, and choose instruments that fit your timeline and risk profile. Build an emergency fund first, use OJK-supervised products, and stay calm when markets move. Consistency matters far more than timing the market.</p>""",
        [("What is a sensible minimum for beginners?", "Start with an amount that doesn't strain your monthly needs, even Rp100,000. The habit and gradual increases matter most."),
         ("Do I need to check my investments every day?", "Not for long-term investing. Reviewing every few months or once a year is enough, making sure your goals and allocation still fit.")]),
    "cara-lapor-spt-tahunan-karyawan": ("""<p>Filing the annual tax return is a routine obligation that is actually simple for employees with one employer. Prepare your withholding slip and list of assets and debts early in the year, file through Coretax before 31 March, and keep the electronic receipt. If you have other income or changed jobs, recalculate the annual tax to avoid underpayment.</p>""",
        [("Do husband and wife file separately?", "It depends on the family's tax status. A wife who chooses to fulfill her own tax obligations (or has separate property) files her own return; if the family's tax obligations are combined, her income is reported in the husband's return. Check the status recorded in Coretax."),
         ("What happens if I don't file?", "There is an administrative fine, and your tax compliance status is recorded as poor, which can affect certain services.")]),
    "cara-menghitung-upah-lembur": ("""<p>Overtime pay follows a clear formula: an hourly wage of 1/173 of monthly wages, with multipliers from 1.5× to 4× depending on the hour and day. Recording your hours, asking for written instructions, and checking your payslip are simple ways to make sure you are paid correctly, while keeping overtime within safe limits for your health.</p>""",
        [("Is overtime on a public holiday the same as on Sunday?", "Yes, both count as overtime on rest days or public holidays with the same multipliers, depending on a 5- or 6-day work week."),
         ("Are contract employees entitled to overtime pay?", "Yes. Overtime rules apply to all employees in an employment relationship, permanent or fixed-term.")]),
    "tips-negosiasi-gaji": ("""<p>Good salary negotiation starts with research, not feelings. Know the market range, separate gross from net, value the benefits, and present your number with solid reasons and a professional attitude. The figure you agree on at the start affects THR, BPJS, and raises for years, so a few hours of preparation is well worth it.</p>""",
        [("When is the best time to discuss salary?", "Usually once the company shows serious interest, such as in the final interview or when receiving an offer."),
         ("What if the offer is below expectations?", "Say thank you, explain the reasons behind your number, and ask whether there is flexibility in salary or other benefits.")]),
    "cara-membuat-anggaran-50-30-20": ("""<p>The 50/30/20 rule gives a simple framework for managing your salary: needs, wants, and savings. The numbers can be adjusted as long as savings come first and spending doesn't exceed income. Start from an accurate net salary, track spending for a few months, and review regularly. Small, consistent habits lead to big changes.</p>""",
        [("Are zakat and charity needs or wants?", "Many people set them aside as a separate item first, before splitting the rest of their income into 50/30/20."),
         ("What if 50% isn't enough for needs?", "Cut wants first, look for ways to lower fixed costs, or increase income. Try to keep some savings even if small.")]),
    "cara-cek-saldo-dan-klaim-jht": ("""<p>Your JHT balance is the result of years of work. Check it regularly through official channels, make sure your data and reported wages are correct, and withdraw only when you truly need it. When changing jobs, merging the balance into your new membership is often the best choice so it keeps growing for retirement.</p>""",
        [("Is there a fee to claim JHT?", "Claims through official BPJS Employment channels are free. Final tax is deducted if the balance exceeds Rp50 million."),
         ("Can someone claim JHT on my behalf?", "For deceased members, heirs file the claim. For other situations, follow the latest official rules on authorization and supporting documents.")]),
    "pinjaman-online-vs-kredit-bank": ("""<p>Online loans offer speed, but at a far higher cost than bank credit. Compare in the same units, calculate the total repayment, and make sure the lender is registered with OJK. Use your emergency fund and other alternatives before borrowing, and if debts have piled up, make a repayment plan as soon as possible.</p>""",
        [("Are all online loans legal?", "No. Only OJK-licensed platforms are legal. Check the official list before applying."),
         ("How can I check my credit history?", "You can request your debtor information (SLIK) through OJK's official service to see the loans recorded under your name.")]),
    "take-over-dan-pelunasan-kpr": ("""<p>Refinancing and early repayment are two effective ways to ease a mortgage, especially when floating rates are high. Calculate the take-over break-even point including all costs, and when prepaying, consider shortening the term for the biggest interest savings. Keep your emergency fund intact and ask for written simulations before deciding.</p>""",
        [("Can I refinance more than once?", "Yes, but each time has costs. Only do it if the rate gap and remaining term are large enough to cover them."),
         ("Does a partial prepayment change the fixed-rate period?", "Usually not, but banks may charge a penalty during the fixed period. Ask about the terms before prepaying.")]),
    "mengenal-sbn-ritel": ("""<p>Retail SBN offer a simple, safe way to invest while funding national development, with coupon and principal payments guaranteed by the state and lower tax than deposits. Choose a series that fits your goal and your view on interest rates, buy through an official distribution partner, and make SBN part of a balanced portfolio.</p>""",
        [("Can SBN coupons change?", "For fixed-coupon series such as ORI and SR, the coupon doesn't change. For SBR and ST, the coupon follows the benchmark rate with a floor."),
         ("Can retail SBN be used as collateral?", "Some series can be pledged under their own terms. Check the information memorandum of the series you buy.")]),
    "reksa-dana-vs-deposito": ("""<p>You don't have to choose between deposits and mutual funds. Deposits give certainty and a guarantee for fixed short-term goals, while mutual funds offer flexibility and higher potential returns depending on the type. Match your choice to your goal, time horizon, and risk profile, then compare net returns after tax and fees.</p>""",
        [("How long does it take to receive money after selling a fund?", "Usually a few working days after redemption, depending on the fund type and the investment manager's terms."),
         ("Are sharia mutual funds different?", "Sharia funds invest in securities that meet sharia principles and are supervised by a Sharia Supervisory Board. They work and carry risks similar to their conventional counterparts.")]),
    "berapa-dana-darurat-yang-ideal": ("""<p>An emergency fund is the foundation that keeps your other financial plans on track when the unexpected happens. Calculate it from essential expenses, adjust for your status and income stability, keep it somewhere safe and accessible, and refill it whenever you use it. Even a small starting target is far better than having nothing.</p>""",
        [("Can an emergency fund be kept in gold?", "Gold can complement it, but its price moves and there is a buy-sell spread. Keep most of the emergency fund in savings or money market funds."),
         ("Do spouses need separate emergency funds?", "Not necessarily. What matters is that the family's total emergency fund covers the household's essential expenses.")]),
}
