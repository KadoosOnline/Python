# دوره برنامه‌نویسی پایتون

نمونه‌کدها و تمرین‌های دوره چهل‌جلسه‌ای برنامه‌نویسی پایتون،
برگزارشده در [مؤسسه فنی و آموزشی کادوس](https://kadoosedu.ir).

دوره از دو ترم تشکیل شده است: ترم اول با نام «مقدمه‌ای بر پایتون» و ترم دوم
با نام «پایتون پیشرفته»، هر کدام بیست جلسه سه ساعته. دوره بدون پیش‌نیاز
شروع می‌شود و در پایان، یک برنامه دسکتاپ کامل با پایگاه داده ساخته می‌شود.
ترتیب جلسه‌ها از ساده به دشوار چیده شده است و هیچ جلسه‌ای از چیزی استفاده
نمی‌کند که در جلسه‌های قبل توضیح داده نشده باشد.

## کتاب دوره

پوشه [`book`](book) یک کتاب چهل‌ویک‌فصلی است که همین دوره را به شکل نوشتاری
و با توضیح کامل پوشش می‌دهد. خودِ کتاب با HTML و CSS ساخته شده است.

- **فصل صفر** مفاهیم پایه را توضیح می‌دهد: برنامه چیست، چرا پایتون، نصب پایتون
  و VS Code، اجرای اولین برنامه و خواندن پیام خطا.
- **فصل‌های یک تا چهل** دقیقاً برابر جلسه‌های همین دوره هستند. هر فصل ابتدا
  موضوع را توضیح می‌دهد، سپس نمونه‌کدها را نشان می‌دهد و بعد آنها را بررسی می‌کند.
- **فصل‌های بیست‌ونه و چهل** جلسه‌های ارزشیابی هستند. مطلب تازه‌ای ندارند و به
  مرور، چک‌لیست آمادگی و نمونه آزمون اختصاص دارند.
- هر فصل با یک جدول جمع‌بندی و چند تمرین عملی تمام می‌شود.

کتاب به شکل آنلاین اینجا در دسترس است و برای خواندنش نیازی به دانلود نیست:

### 📖 [kadoosonline.github.io/Python/book](https://kadoosonline.github.io/Python/book/)

اگر مخزن را دانلود کرده‌اید، فایل [`book/index.html`](book/index.html) را در
مرورگر باز کنید. فهرست مطالب در همان صفحه است و از آنجا به همه فصل‌ها می‌رسید.

نویسنده کتاب: [علیرضا م. احمدی](https://lordarma.com)

## سرفصل جلسه‌ها

### ترم اول: مقدمه‌ای بر پایتون

| پوشه | موضوع |
|------|-------|
| [`S01-first-steps`](S01-first-steps) | چاپ، متغیر، نوع داده، دریافت ورودی، تبدیل نوع و توضیحات |
| [`S02-operators`](S02-operators) | عملگرهای حسابی، انتسابی و مقایسه‌ای، اولویت، تقسیم صحیح و باقی‌مانده |
| [`S03-strings`](S03-strings) | دنباله‌های فرار، اندیس و برش، متدهای رشته و قالب f-string |
| [`S04-conditionals`](S04-conditionals) | نوع بولی، عملگرهای مقایسه و منطقی، دستور if و else |
| [`S05-elif-and-nested-conditionals`](S05-elif-and-nested-conditionals) | elif، شرط تودرتو، عبارت شرطی، match، منو و ماشین‌حساب |
| [`S06-for-loops`](S06-for-loops) | حلقه for، تابع range، الگوی انباشتگر و شمارنده |
| [`S07-nested-loops-and-patterns`](S07-nested-loops-and-patterns) | حلقه‌های تودرتو، جدول ضرب و الگوهای ستاره |
| [`S08-while-loops`](S08-while-loops) | حلقه while، break و continue، حلقه نگهبان و اعتبارسنجی ورودی |
| [`S09-lists`](S09-lists) | ساخت لیست، اندیس و برش، متدهای لیست، تغییرپذیری و دام کپی |
| [`S10-list-algorithms`](S10-list-algorithms) | جمع، میانگین، کمینه و بیشینه، جست‌وجو، مرتب‌سازی و لیست دوبعدی |
| [`S11-functions-basics`](S11-functions-basics) | تعریف تابع، پارامتر، مقدار بازگشتی و فراخوانی |
| [`S12-functions-arguments-and-scope`](S12-functions-arguments-and-scope) | آرگومان پیش‌فرض و کلیدواژه‌ای، حوزه متغیر، تابع main و محافظ اصلی |
| [`S13-functions-advanced`](S13-functions-advanced) | args و kwargs، راهنمای نوع، مستندسازی و بازگشت |
| [`S14-dict-tuple-set`](S14-dict-tuple-set) | دیکشنری، تاپل و مجموعه و متدهای هر کدام |
| [`S15-nested-data-structures`](S15-nested-data-structures) | لیستی از دیکشنری، ماتریس، تبدیل ساختارها و ماژول collections |
| [`S16-standard-library`](S16-standard-library) | کتابخانه استاندارد: random، math، datetime، time و sys |
| [`S17-modules-and-packages`](S17-modules-and-packages) | ماژول شخصی، شکل‌های import، ساخت بسته و فایل init |
| [`S18-files-and-os`](S18-files-and-os) | باز کردن فایل، خواندن و نوشتن و افزودن، دستور with، ماژول os و pathlib |
| [`S19-errors-and-exceptions`](S19-errors-and-exceptions) | try و except و else و finally، raise، assert و ثبت وقایع |
| [`S20-term1-projects`](S20-term1-projects) | پروژه‌های ترم اول: حدس عدد، سنگ کاغذ قیچی، وردل، دوز و آزمون چهارگزینه‌ای |

### ترم دوم: پایتون پیشرفته

| پوشه | موضوع |
|------|-------|
| [`S21-oop-classes-and-objects`](S21-oop-classes-and-objects) | کلاس و شیء، متد سازنده، صفت‌های کلاس و نمونه |
| [`S22-oop-encapsulation-and-dataclasses`](S22-oop-encapsulation-and-dataclasses) | کپسوله‌سازی، property، متد ایستا و کلاسی، ترکیب و dataclass |
| [`S23-oop-inheritance-and-polymorphism`](S23-oop-inheritance-and-polymorphism) | وراثت، super، ترتیب تفکیک متد، چندریختی، تایپ اردکی و کلاس انتزاعی |
| [`S24-oop-magic-methods-and-custom-exceptions`](S24-oop-magic-methods-and-custom-exceptions) | متدهای جادویی، سربارگذاری عملگر و استثناهای سفارشی |
| [`S25-pythonic-code-1`](S25-pythonic-code-1) | جامعیت‌ها، بازکردن، enumerate و zip، for و else، عبارت شرطی و والروس |
| [`S26-pythonic-code-2`](S26-pythonic-code-2) | lambda، map و filter، مرتب‌سازی با کلید، دکوراتور، مولد و itertools |
| [`S27-csv-and-json`](S27-csv-and-json) | خواندن و نوشتن CSV و JSON و ساخت گزارش از داده ساختاریافته |
| [`S28-packages-rest-api-and-xml`](S28-packages-rest-api-and-xml) | محیط مجازی و pip، کتابخانه requests، وب‌سرویس REST، XML و RSS |
| [`S29-evaluation`](S29-evaluation) | جلسه ارزشیابی میان‌ترم |
| [`S30-sql-with-sqlite`](S30-sql-with-sqlite) | زبان SQL: ساخت جدول، درج و به‌روزرسانی، شرط، توابع تجمعی، پیوند و تزریق SQL |
| [`S31-sqlite3-in-python`](S31-sqlite3-in-python) | ماژول sqlite3، چهار عمل اصلی، پرس‌وجوی پارامتری، تراکنش و پشتیبان‌گیری |
| [`S32-orm-and-sqlalchemy`](S32-orm-and-sqlalchemy) | مفهوم ORM، ساخت یک ORM دست‌ساز و سپس مدل‌ها و رابطه‌ها در SQLAlchemy |
| [`S33-design-patterns`](S33-design-patterns) | الگوهای تک‌نمونه، کارخانه، سازنده، مبدل، دکوراتور، استراتژی و ناظر |
| [`S34-tkinter-basics`](S34-tkinter-basics) | پنجره و ویجت‌ها، سه مدیر چیدمان، رویدادها، متغیرهای کنترلی و منو |
| [`S35-tkinter-advanced`](S35-tkinter-advanced) | کار با فایل و تصویر، ویجت‌های ttk، پنجره دوم، بوم نقاشی و یک برنامه دیتابیسی |
| [`S36-pyside6-and-packaging`](S36-pyside6-and-packaging) | کیوت با PySide6، سیگنال و اسلات، Qt Designer و ساخت فایل اجرایی با PyInstaller |
| [`S37-concurrency-threading-asyncio`](S37-concurrency-threading-asyncio) | نخ‌ها، شرایط رقابتی و قفل، صف و استخر نخ، قفل سراسری و asyncio |
| [`S38-flask-web-development`](S38-flask-web-development) | مسیرها، قالب Jinja2، فرم‌ها، نشست و ورود کاربر، وب‌سرویس JSON و پایگاه داده |
| [`S39-capstone-project`](S39-capstone-project) | پروژه پایانی با معماری لایه‌ای، به‌علاوه کنترل نسخه با Git و GitHub |
| [`S40-evaluation`](S40-evaluation) | جلسه ارزشیابی پایانی |

## ساختار پوشه‌ها

هر جلسه یک پوشه است و داخلش نمونه‌های شماره‌گذاری‌شده دارد. در جلسه‌های ابتدایی
هر نمونه یک فایل است و از جایی به بعد، هر نمونه پوشه‌ای با چند فایل می‌شود.

```
S06-for-loops/
├── 01_first_loop.py
├── 02_range.py
...
└── 09_accumulator.py

S34-tkinter-basics/
├── 01_window/
│   └── app.py
├── 02_label/
│   └── app.py
...
└── 13_calculator/
    └── app.py
```

شماره ابتدای هر نمونه، ترتیب آموزشی داخل جلسه را مشخص می‌کند و بهتر است
نمونه‌ها به همان ترتیب خوانده و اجرا شوند. جلسه‌هایی که به کتابخانه بیرونی
نیاز دارند، فایل `requirements.txt` مخصوص خودشان را دارند.

## روش استفاده

۱. مخزن را دانلود یا `clone` کنید.
۲. وارد پوشه جلسه مورد نظر شوید.
۳. فایل نمونه را اجرا کنید:

```bash
python 01_first_loop.py
```

۴. فایل را در ویرایشگر باز کنید، تغییرش دهید و دوباره اجرا کنید.

همین حلقه «بنویس، اجرا کن، تغییر بده» تمام روش کار است. خواندن کد به تنهایی
کافی نیست؛ هر نمونه را خودتان تایپ و اجرا کنید.

برای جلسه‌هایی که کتابخانه بیرونی لازم دارند، ابتدا یک محیط مجازی بسازید:

```bash
python -m venv .venv
.venv\Scripts\activate          # ویندوز
source .venv/bin/activate       # لینوکس و مک
pip install -r requirements.txt
```

## پیش‌نیازها

- پایتون نسخه ۳٫۱۰ یا بالاتر، از [python.org](https://www.python.org).
  در ویندوز هنگام نصب، گزینه **Add python.exe to PATH** را حتماً تیک بزنید.
- یک ویرایشگر کد. پیشنهاد ما [VS Code](https://code.visualstudio.com) است.
- برای بیست جلسه اول هیچ چیز دیگری لازم نیست؛ همه چیز با خود پایتون کار می‌کند.
- در لینوکس، جلسه‌های ۳۴ و ۳۵ ممکن است به نصب جداگانه tkinter نیاز داشته باشند:
  `sudo apt install python3-tk`

## نکته‌های فنی

- همه توضیحات و مستندات داخل کد به **انگلیسی** نوشته شده‌اند تا کد با هر
  ویرایشگر و هر سیستمی بدون مشکل نمایش داده شود.
- سبک کد یکدست است: تورفتگی چهار فاصله، نام‌گذاری `snake_case`، تابع `main` و
  محافظ `__name__` از جلسه دوازدهم و راهنمای نوع از جلسه سیزدهم به بعد.
- همه فایل‌های متنی با `utf-8` باز می‌شوند تا متن فارسی درست خوانده شود.
- **هیچ توکن، رمز یا کلیدی در کد نوشته نشده است.** جلسه سی‌وهفتم نشان می‌دهد
  چرا این مقادیر باید از متغیر محیطی خوانده شوند.
- کتاب هیچ فایلی از اینترنت نمی‌خواند و روی کامپیوتر بدون اینترنت هم کامل
  کار می‌کند.

## نویسنده

[علیرضا م. احمدی](https://lordarma.com)

تهیه‌شده برای [مؤسسه فنی و آموزشی کادوس](https://kadoosedu.ir).
