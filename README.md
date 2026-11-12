# FinNova Wallet (web build)

Live demo: **https://tngfranklin.github.io/finnova-web/**

FinNova Wallet is a cross-platform Flutter demo banking app for the FinNova Bank platform:
digital wallet, peer-to-peer transfers, QR payments and a payment history, protected by
email + password and a simulated SMS one-time code.

This repository only contains the compiled web build that GitHub Pages serves. The app is a
demo: wallets, balances and history are stored locally on each device (the visitor's browser or phone),
and the SMS code is simulated on screen. The only thing shared between devices is the payment relay (below), so a QR code shown on one device can be paid from another.

**Try it:** open the live demo and tap **Use** on the demo account card on the sign-in screen,
then enter the simulated code shown in the notification at the top of the screen.

**Android app:** download **[finnova.apk](https://tngfranklin.github.io/finnova-web/finnova.apk)** on
your phone and install it (allow installing from your browser when Android asks). It is a
sandbox demo signed with a debug key, so Play Protect may warn that it is from an unknown
developer. In the app, **Scan & pay** uses the camera to pay the QR code shown on
**My QR code** in the web demo.

## Screenshots

| Sign in | Two-step verification |
| --- | --- |
| ![Sign in](screenshots/01-login.jpg) | ![Verification code](screenshots/02-otp-verification.jpg) |

| Wallet | Quick actions and recent activity |
| --- | --- |
| ![Wallet](screenshots/03-wallet.jpg) | ![Actions and activity](screenshots/04-wallet-actions-activity.jpg) |

| Send money | My QR code |
| --- | --- |
| ![Send money](screenshots/05-send-money.jpg) | ![My QR code](screenshots/06-my-qr-code.jpg) |

| Payment history | Transaction details |
| --- | --- |
| ![Payment history](screenshots/07-payment-history.jpg) | ![Transaction details](screenshots/08-transaction-details.jpg) |

## Related

The FinNova Bank REST API (Node.js, PostgreSQL, Docker, deployed to Azure App Service with
GitHub Actions) is a separate project. The app calls only its `/relay` routes: on sign-in each wallet registers its name there, scanning a QR looks the payee up, and payments wait in the payee's inbox until their device collects them (about every 10 seconds). Balances are not held by the server, so this is for demo money only. The free Azure plan sleeps when idle, so the first request can take up to a minute.
