.. _api-reference:

==============
API Reference
==============

Core application components
---------------------------

=============================================== ========================
 Component                                       Description
=============================================== ========================
 :doc:`Application </reference/api/app>`         The application itself
 :doc:`Window </reference/api/window>`           Window object
 :doc:`MainWindow </reference/api/mainwindow>`   Main Window
=============================================== ========================

General widgets
---------------

======================================================================= ========================================================================
 Component                                                               Description
======================================================================= ========================================================================
 :doc:`ActivityIndicator </reference/api/widgets/activityindicator>`     A small animated indicator showing activity on a task of indeterminate
                                                                         length, usually rendered as a "spinner" animation.
 :doc:`Button </reference/api/widgets/button>`                           A button that can be pressed or clicked.
 :doc:`Canvas </reference/api/widgets/canvas>`                           Area you can draw on
 :doc:`DetailedList </reference/api/widgets/detailedlist>`               A list of complex content
 :doc:`Divider </reference/api/widgets/divider>`                         A separator used to visually distinguish two sections of content in a
                                                                         layout.
 :doc:`ImageView </reference/api/widgets/imageview>`                     Image Viewer
 :doc:`Label </reference/api/widgets/label>`                             A text label for annotating forms or interfaces.
 :doc:`MultilineTextInput </reference/api/widgets/multilinetextinput>`   A scrollable panel that allows for the display and editing of multiple
                                                                         lines of text.
 :doc:`NumberInput </reference/api/widgets/numberinput>`                 A text input that is limited to numeric input.
 :doc:`PasswordInput </reference/api/widgets/passwordinput>`             A widget to allow the entry of a password. Any value typed by the
                                                                         user will be obscured, allowing the user to see the number of
                                                                         characters they have typed, but not the actual characters.
 :doc:`ProgressBar </reference/api/widgets/progressbar>`                 A horizontal bar to visualize task progress. The task being monitored
                                                                         can be of known or indeterminate length.
 :doc:`Selection </reference/api/widgets/selection>`                     Selection
 :doc:`Slider </reference/api/widgets/slider>`                           A widget for selecting a value within a range. The range is shown as a
                                                                         horizontal line, and the selected value is shown as a draggable marker.
 :doc:`Switch </reference/api/widgets/switch>`                           A clickable button with two stable states: True (on, checked); and
                                                                         False (off, unchecked). The button has a text label.
 :doc:`Table </reference/api/widgets/table>`                             Table of data
 :doc:`TextInput </reference/api/widgets/textinput>`                     A widget for the display and editing of a single line of text.
 :doc:`Tree </reference/api/widgets/tree>`                               Tree of data
 :doc:`WebView </reference/api/widgets/webview>`                         A panel for displaying HTML
 :doc:`Widget </reference/api/widgets/widget>`                           The abstract base class of all widgets. This class should not be be
                                                                         instantiated directly.
======================================================================= ========================================================================

Layout widgets
--------------

==================================================================== ========================================================================
 Usage                                                                Description
==================================================================== ========================================================================
 :doc:`Box </reference/api/containers/box>`                           A generic container for other widgets. Used to construct layouts.
 :doc:`ScrollContainer </reference/api/containers/scrollcontainer>`   Scrollable Container
 :doc:`SplitContainer </reference/api/containers/splitcontainer>`     Split Container
 :doc:`OptionContainer </reference/api/containers/optioncontainer>`   Option Container
==================================================================== ========================================================================

Resources
---------

========================================================= ========================================================================
 Component                                                 Description
========================================================= ========================================================================
 :doc:`App Paths </reference/api/resources/app_paths>`     A mechanism for obtaining platform-appropriate file system locations
                                                           for an application.
 :doc:`Font </reference/api/resources/fonts>`              Fonts
 :doc:`Command </reference/api/resources/command>`         Command
 :doc:`Group </reference/api/resources/group>`             Command group
 :doc:`Icon </reference/api/resources/icons>`              An icon for buttons, menus, etc
 :doc:`Image </reference/api/resources/images>`            An image
 :doc:`Validators </reference/api/resources/validators>`   A mechanism for validating that input meets a given set of criteria.
========================================================= ========================================================================

.. toctree::
   :hidden:

   app
   mainwindow
   window
   containers/index
   resources/index
   widgets/index
