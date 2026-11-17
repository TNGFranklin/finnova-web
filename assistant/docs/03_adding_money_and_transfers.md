# FinNova Wallet: Adding Money, Transfers and Mobile Money

## Adding money (top-up)
Open the Top up page, choose the currency balance and then a method. Methods are matched to the currency, with the most common local method first and the card last.

| Currency | Methods |
|----------|---------|
| EUR | SEPA Instant pay by bank, iDEAL / Wero, PayPal, card |
| USD | US bank account (ACH), PayPal, card |
| GBP | UK pay by bank (Faster Payments), PayPal, card |
| KES | M-Pesa, Airtel Money, PesaLink, card |
| UGX | Airtel Money, MTN MoMo, card |
| TZS | M-Pesa, Airtel Money, Mixx by Yas, card |
| NGN | Bank transfer, USSD, card |
| GHS | MTN MoMo, Telecel Cash, card |
| ZAR | PayShap / Instant EFT, card |
| INR | UPI, net banking, card |
| HUF | Instant bank transfer, card |

How approval works:
- Mobile money (M-Pesa, Airtel Money, MTN MoMo, Telecel Cash, Mixx): a request is sent to your phone and you approve it with your PIN.
- PayPal: you approve the payment in PayPal.
- UPI: you approve the collect request in your UPI app with your UPI PIN.
- Pay by bank: you pick your bank and approve in your banking app.
- USSD: you dial a short code on the phone registered with your bank.
- Card: the card form is checked by the card gateway.

Arrival times: most methods are instant or within seconds. SEPA Instant and UK Faster Payments arrive within seconds, a Nigerian bank transfer within a minute, a Hungarian instant transfer within 5 seconds, and a US ACH transfer in 1 to 3 business days (instant with RTP or FedNow).

## Sending money to another FinNova member
1. Open Transfer and enter the recipient's wallet, or scan their payment QR code.
2. Enter the amount and an optional note, then confirm.
3. The money moves immediately and both members see it in their history.

There is no fee. Payments of 50.00 or more need a one-time code (see the Security document).

## Payment QR codes
Each member can generate a payment QR code. The code is a link to the FinNova web app, so a phone camera or Google Lens can open it. If you are not signed in, the payment is kept until you sign in. Scanning a QR code that is not a FinNova payment code is rejected.

## Wallet relay between devices
Separate installs, such as a phone and a browser, find each other through the FinNova Bank API wallet relay, so a member on a phone can pay a member on the website.

## Mobile money, cash pickup and bank transfers
To send money to an M-Pesa, Airtel Money or MTN MoMo number, or to a bank, do not use the Transfer page. Use the Mobile money page: open Mobile money, choose the service (for example M-Pesa), enter the recipient's mobile number, choose the currency to send from, enter the amount, check the fee, exchange rate and what the recipient gets, then confirm.

The Mobile money page sends money out of your account:
- Mobile money wallets: M-Pesa (KES), Airtel Money (KES, UGX, TZS), MTN MoMo (UGX, GHS). The recipient is identified by mobile number.
- Cash pickup: Western Union and MoneyGram, identified by the receiver's full name as on their ID. Cash is ready for pickup in minutes.
- PayPal: send to any PayPal email in EUR, USD or GBP.
- Bank transfers: SEPA (IBAN, seconds with SEPA Instant otherwise the next business day), UK Faster Payments (8-digit account number and 6-digit sort code, usually within 2 hours), SWIFT (account number or IBAN and an 8 or 11 character SWIFT/BIC code, 1 to 3 business days).

Before you send, the app shows the fee, the exchange rate and exactly how much the recipient gets. You can send from any currency balance. If your balance is too short the app says how much you need including the fee. After sending you receive a confirmation code in the style of the service, for example an MTCN for Western Union.

## Receipts and history
Every transaction appears in History and has a receipt that can be downloaded.
