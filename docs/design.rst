
.. default-domain:: py

AASHE Resource Center Design Document
=====================================

This design document captures the requirements for an AASHE resource
center Django project. This project is part of the resource center
database-conversion project. The goal is to write a quick port of an
existing set of static resource pages to a database-driven Django
application. 

Resource pages are to be crawled and their content automatically
populated into essentially identical database-driven pages. The
resource center application is expected to evolve substantially from
this initial design.


Requirements
------------

The AASHE Resource Center generally contains three-levels of
categories to organize content. The categories as they exist at the
time of writing are (generally) based on the STARS reporting system's
credit categorization. The existing categories are outlined below.

- General Resources for Campus Sustainability

  - AASHE Bulletin Database

  - Campus Profiles

  - Case Study Database

  - Organizations

  - Resources for Students

  - Sustainability Events Calendar

  - AASHE Conference Materials

  - Campus Sustainability Blogs

  - Discussion Lists and e-Newsletters

  - Publications (Articles, Journals, etc.)

  - Resources for Campus Sustainability Officers

- Education & Research Resources

  - Co-Curricular Education and Student Organizing

  - Curriculum

  - Research

- Campus Operations Resources

  - Buildings

  - Dining Services

  - Grounds

  - Transportation

  - Water

  - Climate

  - Energy

  - Purchasing

  - Waste

- Planning, Administration & Engagement Resources

  - Assessment tools, reports, indicators

  - Human Resources

  - Coordination & Planning

  - Policies

  - Investment & Financing

  - Affordability and Access

  - Diversity and Inclusion

  - Public Engagement

- AASHE Publications

  - AASHE Bulletin

  - AASHE HE Sustainability Reviews

  - AASHE Monographs

  - AASHE Newsletters

  - AASHE Surveys

  - Wiki Books

  - AASHE-Partnered Publications

Within the second-level resource center pages, a variety of formatting
exists. Generally the formatting is in the form of a section heading,
an opening paragraph of descriptive text ("happy talk"), followed by
sub-heading categorizations with a list of resources beneath each. For
example::

  <h1>Second-level Section Heading</h1>

  <p>Introductory paragraph text that includes a description of these
  resources that follow and other pointers, images, etc.</p>

  <h2>AASHE Lists & Databases</h2>

  <ul>
    <li><a href="http://external.com">External Link</a></li>
    <li><a href="http://external.com">External Link</a></li>
    <li><a href="http://external.com">External Link</a></li>
  </ul>

  <h2>News, Research & Publications</h2>
  <ul>
    <li><a href="http://external.com">External Link</a></li>
    <li><a href="http://external.com">External Link</a></li>
    <li><a href="http://external.com">External Link</a></li>
  </ul>

  <p>Closing text with "Please email" address for questions & updates</p>

The links that comprise the "third level" landing pages are a mixed
group. Some are external links to resources at other sites, others are
links to existing AASHE databases and/or other resource pages, and
some lead to anther landing page that has a structure similar to the
third-level pages. The new resource center system would ideally allow
for additional levels beyond 3 in a simple and automatic way.

Page Parsers
^^^^^^^^^^^^

To facilitate the transition from static content, Python-based screen
scraping scripts will be used. These employ the ``BeautifulSoup``
library to download and parse the HTML markup of each resource center
page.


High-level Entities
-------------------

CMS App
^^^^^^^

The CMS app is responsible for handling the resource center's
non-resource content, which is mostly landing pages and other
indexes. Resource pages will be handled separately by Django views and
templates.

  .. class:: Page

     Pages contain content, including descriptive language or
     guidance as to the use of a particular set of resources. They also
     contain a set of links. This set of links is captured in an
     associated `Menu` object.

  .. class:: Menu

     Menus are a set of links, in a hierarchy, that are able to
     be associated to a Page. Menus will be implemented using the 
     ``django-treemenus`` third-party app 
     (http://github.com/jphalip/django-treemenus).

Resources App
^^^^^^^^^^^^^

The resources app stores the models and helper functions for
database-driven resources. This includes an abstract base model that
can be extended by specific resources to suit their individual
requirements. 


Low-level Entity Design
-----------------------

CMS
^^^

.. class:: Page

   ``Page`` models are simple CMS page objects that contain the following
   fields:

   .. attribute:: title

      The Page's title. This is rendered by the template appropriately,
      including in HTML title tags.

   .. attribute:: path

      The Page's URL path as a ``SlugField`` (letters, numbers,
      underscores or hyphens). 

   .. attribute:: published

      Is the Page published?

   .. attribute:: pub_date

      Date & time the page was published. Set by a custom save() method.

   .. attribute:: created_date

      `Auto_now_add` field to set the creation date & time.

   .. attribute:: updated_date

      `Auto_now` field to set the updated date & time.

   .. attribute:: content

      A field to contain the page's content. This will not include the
      menu of links. It is a `TextField` but it's intended to contain
      formatting in Markdown syntax.

   .. attribute:: menu

      A related Menu object. The menu will be displayed beneath the
      Page's content when rendered by the template.

Resources
^^^^^^^^^

.. class:: ResourceItem

   The ``ResourceItem`` model is an abstract base class to be extended
   by actual resource information models.

   .. attribute:: title 

     The title of the resource item, e.g. the name of an externally
     linked webpage resource, a wind turbine installation, etc.

   .. attribute:: url

     The resource item's URL link. 

   .. attribute:: description

     Descriptive text for this resource item.

   .. attribute:: published

      Is the Page published?

   .. attribute:: pub_date

      Date & time the page was published. Set by a custom save() method.

   .. attribute:: created_date

      `Auto_now_add` field to set the creation date & time.

   .. attribute:: updated_date

      `Auto_now` field to set the updated date & time.

   .. attribute:: notes

      An internal notes field for staff use.

.. class:: ResourceItemManager

   By default, the ``ResourceItem`` class, and any sub-class that
   extends it, will be given this Django manager. It will be used for
   common filtering operations and other behaviors.

   .. method:: published(self)
   
      Return a chainable, filtered QuerySet including only published
      items (items with ``published == True``).
   

Resource models
^^^^^^^^^^^^^^^

Resource models extend the ``ResourceItem`` base class with additional
fields and behaviors as needed. 
