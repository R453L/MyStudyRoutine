# 📖 EEE Study Bot — সম্পূর্ণ Setup Tutorial

## ফাইল স্ট্রাকচার

```
your-repo/
├── bot.py
└── .github/
    └── workflows/
        └── daily_routine.yml
```

-----

## ধাপ ১ — Telegram Bot তৈরি করো

1. Telegram এ **@BotFather** খোলো
1. `/newbot` লিখে পাঠাও
1. Bot এর নাম দাও (যেমন: `EEE Study Bot`)
1. Username দাও (যেমন: `eee_study_rasel_bot`)
1. BotFather তোমাকে একটা **TOKEN** দেবে → এটা সেভ করো
   
   ```
   উদাহরণ: 7123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

-----

## ধাপ ২ — Telegram Group তৈরি ও Bot Add করো

1. Telegram এ একটা **নতুন Private Group** তৈরি করো
1. Group এ তোমার bot কে **Admin** বানাও
- Group Settings → Administrators → Add Administrator
- **Pin Messages** permission অবশ্যই দিতে হবে ✅
1. Group এর **Chat ID** বের করো:
- Browser এ যাও: `https://api.telegram.org/bot<TOKEN>/getUpdates`
- Group এ যেকোনো message পাঠাও
- JSON এ `"chat":{"id":` এর পরের নম্বরটা নাও
- Group ID সবসময় **negative** হয়, যেমন: `-1001234567890`

-----

## ধাপ ৩ — GitHub Repository তৈরি করো

1. **github.com** এ নতুন **Private repository** খোলো
1. নাম দাও: `eee-study-bot`
1. দুটো ফাইল upload করো:
- `bot.py` → root এ
- `.github/workflows/daily_routine.yml` → এই path এ

> ⚠️ `.github` ফোল্ডার hidden, manually তৈরি করতে হবে অথবা
> GitHub এ “Create new file” দিয়ে path লিখলেই folder তৈরি হয়।

-----

## ধাপ ৪ — GitHub Secrets সেট করো

1. Repository → **Settings** → **Secrets and variables** → **Actions**
1. **New repository secret** চাপো
1. দুটো secret যোগ করো:

|Name       |Value                             |
|-----------|----------------------------------|
|`BOT_TOKEN`|BotFather থেকে পাওয়া token            |
|`CHAT_ID`  |Group এর chat id (negative number)|

-----

## ধাপ ৫ — Test করো

1. Repository → **Actions** tab এ যাও
1. **Daily Study Routine** workflow দেখবে
1. **Run workflow** বাটন চাপো
1. কিছুক্ষণ পরে তোমার Telegram group এ message আসবে ও pin হবে ✅

-----

## কিভাবে কাজ করে

```
প্রতিদিন ভোর ৪টা (Bangladesh)
        ↓
GitHub Actions জেগে ওঠে
        ↓
state.json থেকে আজকের index পড়ে
        ↓
EEE + Non-Dept থেকে random topic বাছাই
        ↓
Telegram group এ message পাঠায়
        ↓
Message pin করে
        ↓
state.json update করে (পরের দিনের জন্য)
        ↓
৭ দিন পর নতুন shuffle শুরু হয়
```

-----

## Shuffle System

- প্রতি সপ্তাহে EEE ও Non-Dept আলাদাভাবে **random shuffle** হয়
- মানে এই সপ্তাহে শনিবারে DC Circuit থাকলে
  পরের সপ্তাহে যেকোনো দিন আসতে পারে
- EEE ও Non-Dept এর shuffle **independent** — একটার সাথে আরেকটার মিল নেই

-----

## সমস্যা হলে

**Message আসছে না?**

- BOT_TOKEN ও CHAT_ID ঠিক আছে কিনা দেখো
- Bot কে group এ Admin করা হয়েছে কিনা দেখো

**Pin হচ্ছে না?**

- Bot এর “Pin Messages” permission আছে কিনা দেখো

**Actions চলছে না?**

- GitHub free account এ Actions enabled আছে কিনা দেখো
- Repository → Settings → Actions → Allow all actions

-----

## ভবিষ্যতে Quiz যোগ করতে চাইলে

`bot.py` তে শুধু একটা নতুন function যোগ করলেই হবে।
বললে তখন আপডেট করে দেব! 🎯