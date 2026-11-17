# FinNova Wallet: Accounts and Currencies

## Who can open an account
Anyone can register in the FinNova Wallet app with a name, email address, mobile number and password. Every member receives one wallet, identified by a wallet ID. Registering takes a few minutes and no branch visit is needed.

## Multicurrency account
One FinNova account holds a separate balance for each supported currency. The main wallet currency is the euro (EUR). The supported currencies are:

| Code | Currency | Country or region |
|------|----------|-------------------|
| EUR | Euro | Eurozone |
| USD | US dollar | United States |
| GBP | British pound | United Kingdom |
| KES | Kenyan shilling | Kenya |
| UGX | Ugandan shilling | Uganda |
| TZS | Tanzanian shilling | Tanzania |
| NGN | Nigerian naira | Nigeria |
| GHS | Ghanaian cedi | Ghana |
| ZAR | South African rand | South Africa |
| INR | Indian rupee | India |
| HUF | Hungarian forint | Hungary |

Money can be moved between your own currency balances on the Currencies page. Conversions use live market exchange rates when they are available, and built-in reference rates otherwise. A conversion fee of 0.5 % applies (see the Fees document).

## Account numbers
Each member gets one account number per currency. The format is `FN`, two check digits, the three-letter currency code and ten digits taken from the wallet ID. Example: `FN47GBP0000001001`.

- The number is unique to the member and the currency. The same number never appears in two currencies.
- The two check digits use the same mod-97 method as an IBAN, so a mistyped account number is detected before any money moves.
- Account numbers are shown on the Profile page and in the account details card, where they can be copied or shared.

## Profile and account details
The Profile page shows the member's name, email, mobile number, wallet ID and account numbers. Account details can be shared with someone who wants to pay you.

## Mobile number registry
A mobile number belongs to one member only. If a number is already registered to another member, registration with that number is refused.

## Sandbox mode
FinNova Wallet is a demonstration bank. All payment providers (card gateway, M-Pesa, PayPal, SWIFT and others) run in sandbox mode: confirmation codes are generated locally and no real money moves.
