# 100 Days Of Code - Log
## This is my first round of 100DaysOfCode Challege. Entails, minimal of 1 hour of coding Monday to Sunday from 19th, Oct 2021 to 27th, Jan 2022.
## Covering Django Framework.
<a name="toc"></a>
### Table of Contents
|Day|Topic|Day|Topic
|:---:|:-----:|:---:|:-----:|
|[Day 1](#day-1) **19th Oct 2021**|Django Class Base Views: Thread safety with view arguments - Passing immutable object as an argument to a view to avoid different output from same view when utilized in concurrent or muilt-threading environment.|[Day 2](#day-2) **20th Oct 2021**|Design:Pagination and Inifinite Scrolling. Django CBVs continuation. 
|[Day 3](#day-3) **21 Oct 2021**|Django Topics of the Day: Class Base Views, CBV's decorators and mixins usage.|[Day 4](#day-4) **22 Oct 2021**|Topic Covered Today: CBVs mixins and their methods; Simple mixins, Single object mixins, Muiltiple object mixins and so on.
|[Day 5](#day-5) **23 Oct 2021**|Django Form handling with Class Based Views. Editing mixins. Track user that created an object using a CreateView.|[Day 6](#day-6) **24 Oct 2021**| Django Class Based Views Continuation. Combining mixins with other mixins, and mixins with generic CBVs to get desired functionality.
|[Day 7](#day-7) **25 Oct 2021**|Topics Covered: Context and template responses(CBVs) with JSONResponseMixin and Pagination.|[Day 8](#day-8) **26 Oct 2021**|More practise on CBVs, JsonResponse, Pagination and Mixins.|[Day 8](#day-8) **26 Oct 2021**|More practise on CBVs mixins' attributes and methods.
|[Day 9](#day-9) **27 Oct 2021**|Django Topic of the day: I decided to stay a little longer on Class Base Views to gain more insight probably make some more errors and learn from them.|[Day 10](#day-10) **28 Oct 2021**|Topic of the day: Concluded on CBVs-Built-in display views, Built-in editing views, Using mixins.
|[Day 11](#day-11) **29 Oct 2021**|Django Topics:Making queries(CRUD), using Django Queryset methods and fields lookup keyword arguments.|[Day 12](#day-12) **30 Oct 2021**|Topic Covered: Caching and QuerySet and F() Expressions.
|[Day 13](#day-13) **31 Oct 2021**|Topic Covered: More practise on F(). Using F() to reference fields on the models and so on.|[Day 14](#day-14) **1st Nov 2021**|Topics covered: Avoiding Race Conditions and Reducing the number of queries in some operations using F(), Creating Dynamic fields on model using Annotations, F(), & ExpressionWrapper.
|[Day 15](#day-15) **2nd Nov 2021**|Topic covered: More Practice on using F() with Filters, Annotations and sorting null value.|[Day 16](#day-16) **3rd Nov 2021**|Topic: More Practice on Query Expressions.
|[Day 17](#day-17) **4th Nov 2021**|Topics: Nesting Query Expressions and annotating with Sum, Max, Min, Avg and so on.|[Day 18](#day-18) **5th Nov 2021**|Topic: Query Expressions continuation with Q.
|[Day 19](#day-19) **6th Nov 2021**|Topics: More on Query Expressions.|[Day 20](#day-20) **7th Nov 2021**|Topic: More practice on Query Expressions.
|[Day 21](#day-21) **8th Nov 2021**|Topic Covered: Querying JSONField; Storing and querying for None, & Key, index, and path transforms.|[Day 22](#day-22) **9th Nov 2021**|Topics:Copying model instances, Updating multiple objects at once and Related objects.
|[Day 23](#day-23) **10th Nov 2021**|Topics QuerySet API reference. |[Day 24](#day-24) **11th Nov 2021**|Topics: Writing Tests.
|[Day 25](#day-25) **16th Nov 2021**|Covered: Recap on Writing and Running Tests.|[Day 26](#day-26) **17th Nov 2021**|Topic: Recap on Python re module and more practice on Writing and running tests Django.
|[Day 27](#day-27) **18th Nov 2021**|Topics: Python Unittest Module.|[Day 28](#day-28) **19th Nov 2021**|Topics: Unit Testing Framework-Python Mock and Polymorphism in python.
|[Day 29](#day-29) **20th Nov 2021**|Covered: Started working on Online Movie Ticket Booking System(Python/Django).|[Day 30](#day-30) **21st Nov 2021**|Covered: Worked on my project's(Online Movie Ticket Booking System) model layer.
|[Day 31](#day-31) **22nd Nov 2021**|Worked On (Online Movie Ticket Booking System) Model layer and a little bit on Template and View layer.|[Day 32](#day-32) **23rd Nov 2021**|Topics: Worked on the Templates and Views.
|[Day 33](#day-33) **24th Nov 2021**|Topics: Started writing tests for my project(TDD).|[Day 34](#day-34) **25th Nov 2021**|Topics: Worked on Templates Layer.
|[Day 35](#day-35) **26th Nov 2021**|Covered: HTML, CSS, and Django: worked on my project's views and templates.|[Day 36](#day-36) **27th Nov 2021**|Topics: Worked on Django JsonResponse(view) by implementing Ajax in JQuery.
|[Day 37](#day-37) **28th Nov 2021**|Topic: Worked on my project's list view touching up some js, css, html and django functionalities.|[Day 38](#day-38) **29th Nov 2021**|Topics: Forms overview, Form API, and Built-in fields.
|[Day 39](#day-39) **30th Nov 2021**|Topics: Django: CSRF Defense and a little bit on Cookies and Sessions.|[Day 40](#day-40) **01st Dec 2021**|Topics: Started Django’s cache framework.
|[Day 41](#day-41) **02nd Dec 2021**|Topics: Still on Django’s cache framework.  |[Day 42](#day-42) **03rd Dec 2021**|Topics: Still on Django cache framework. Extras: One challenge a day at Sololearn Coding challenges(Python)
|[Day 43](#day-43) **04th Dec 2021**|Topics: Django cache framework continuation. |[Day 44](#day-44) **05th Dec 2021**|Topics:The low-level cache API.
|[Day 45](#day-45) **06th Dec 2021**|Topics: Cache key prefixing, Cache versioning & Cache key transformation.|[Day 46](#day-46) **07th Dec 2021**|Topics: Low-Level Cache API(Polishing).
|[Day 47](#day-47) **08th Dec 2021**|Topics: Django: Low-Level Cache API- Invalidating cache objects.|[Day 48](#day-48) **09th Dec 2021**|Topics: Signals.
|[Day 49](#day-49) **10th Dec 2021**|Topics:Using signals to invalidate cache.|[Day 50](#day-50) **11th Dec 2021**|Topics: Concluded on Django signals at least for now.
|[Day 51](#day-51) **12th Dec 2021**|Topics: Sessions.|[Day 52](#day-52) **13th Dec 2021**|Topics: Using sessions in views.
|[Day 53](#day-53) **14th Dec 2021**|Topics: Sessions.|[Day 54](#day-54) **15th Dec 2021**|Topics: Sessions(Session security).
|[Day 55](#day-55) **16th Dec 2021**|Topics: Django: Sessions(Using sessions out of views). |[Day 56](#day-56) **18th Dec 2021**|Topics: Still handling Django Sessions.
|[Day 57](#day-57) **19th Dec 2021**|Topics: Concluded Sessions (for now). |[Day 58](#day-58) **20th Dec 2021**|Topics: Started Security in Django-Cross site scripting (XSS) protection.
|[Day 59](#day-59) **21th Dec 2021**|Topics: Data Structures(Linked List and Reverse Linked List).Revised Recursion. |[Day 60](#day-60) **22th Dec 2021**|Topics:  Security in Django. Data Structures(Python)
|[Day 61](#day-61) **23th Dec 2021**|Topics: Data Structures(Doubly Linked List). Security in Django. |[Day 62](#day-62) **24th Dec 2021**|Topics: Security in Django (protecting the SECRET_KEY). Data Structures(Still on Doubly Linked List).
|[Day 63](#day-63) **26th Dec 2021**|Topics: Security in Django (Serialization(Pickle, YAML, XML) Vulnerabilities). Data Structures(Doubly Linked List). |[Day 64](#day-64) **27th Dec 2021**|Topics: Security in Django (Cryptographic Signing). Data Structures(Concluded Doubly Linked List) at least for now.
|[Day 65](#day-65) **28th Dec 2021**|Topics: Security in Django (Cross Site Scripting (XSS) Protection).Data Structures practice at GeeksforGeeks.|[Day 66](#day-66) **29th Dec 2021**|Topics:  Security in Django (Concluded on Cross-site scripting (XSS) protection). Data Structures Circular Linked List(Python)
