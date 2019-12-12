# PySImpleGUI Keynotes

## Popups

``` python
sg.Popup('Popup')  # Shows OK button
sg.PopupOk('PopupOk')  # Shows OK button
sg.PopupYesNo('PopupYesNo')  # Shows Yes and No buttons
sg.PopupCancel('PopupCancel')  # Shows Cancelled button
sg.PopupOKCancel('PopupOKCancel')  # Shows OK and Cancel buttons
sg.PopupError('PopupError')  # Shows red error button
sg.PopupTimed('PopupTimed')  # Automatically closes
sg.PopupAutoClose('PopupAutoClose')  # Same as PopupTimed
PopupScrolled()
```

## Core Elements List

* Buttons including these types:
  * File Browse
  * Folder Browse
  * Color chooser
  * Date picker
  * Read window
  * Close window
  * Realtime
* Checkbox
* Radio Button
* Listbox
* Slider
* Multi-line Text Input
* Scroll-able Output
* Progress Bar
* Option Menu
* Image
* Menu
* Frame
* Column
* Graph
* Table
* Tabbed windows
* Redirected Python Output/Errors to scrolling Window

## Events

| Name             | events                |
| ---------------- | --------------------- |
| InputText        | any change            |
| Combo            | item chosen           |
| Listbox          | selection changed     |
| Radio            | selection changed     |
| Checkbox         | selection changed     |
| Spinner          | new item selected     |
| Multiline        | any change            |
| Text             | clicked               |
| Status Bar       | clicked               |
| Graph            | clicked               |
| Graph            | dragged               |
| Graph            | drag ended (mouse up) |
| TabGroup         | tab clicked           |
| Slider           | slider moved          |
| Table            | row selected          |
| Tree             | node selected         |
| ButtonMenu       | menu item chosen      |
| Right click menu | menu item chosen      |
