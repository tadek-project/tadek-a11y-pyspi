################################################################################
##                                                                            ##
## This file is a part of TADEK.                                              ##
##                                                                            ##
## TADEK - Test Automation in a Distributed Environment                       ##
## (http://tadek.comarch.com)                                                 ##
##                                                                            ##
## Copyright (C) 2011 Comarch S.A.                                            ##
## All rights reserved.                                                       ##
##                                                                            ##
## TADEK is free software for non-commercial purposes. For commercial ones    ##
## we offer a commercial license. Please check http://tadek.comarch.com for   ##
## details or write to tadek-licenses@comarch.com                             ##
##                                                                            ##
## You can redistribute it and/or modify it under the terms of the            ##
## GNU General Public License as published by the Free Software Foundation,   ##
## either version 3 of the License, or (at your option) any later version.    ##
##                                                                            ##
## TADEK is distributed in the hope that it will be useful,                   ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of             ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ##
## GNU General Public License for more details.                               ##
##                                                                            ##
## You should have received a copy of the GNU General Public License          ##
## along with TADEK bundled with this file in the file LICENSE.               ##
## If not, see http://www.gnu.org/licenses/.                                  ##
##                                                                            ##
## Please notice that Contributor Agreement applies to any contribution       ##
## you make to TADEK. The Agreement must be completed, signed and sent        ##
## to Comarch before any contribution is made. You should have received       ##
## a copy of Contribution Agreement along with TADEK bundled with this file   ##
## in the file CONTRIBUTION_AGREEMENT.pdf or see http://tadek.comarch.com     ##
## or write to tadek-licenses@comarch.com                                     ##
##                                                                            ##
################################################################################

import atspi

from interface import *
from constants import *

_DESKTOP = 0

#
# Implement accessibility constants:
#
actionset = ActionSet()
actionset.ACTIVATE = "activate"
actionset.CLICK = "click"
actionset.CONTRACT = "expand or contract"
actionset.EDIT = "edit"
actionset.EXPAND = "expand or contract"
actionset.PRESS = "press"
actionset.RELEASE = "release"

buttonset = ButtonSet()
buttonset.LEFT = 1
buttonset.MIDDLE = 2
buttonset.RIGHT = 3

relationset = RelationSet()
relationset.CHILD_CELL_OF = atspi.SPI_RELATION_NODE_CHILD_OF
relationset.LABEL_FOR = atspi.SPI_RELATION_LABEL_FOR
relationset.LABELED_BY = atspi.SPI_RELATION_LABELED_BY

roleset = RoleSet()
roleset.ACCELERATOR_LABEL = atspi.SPI_ROLE_ACCEL_LABEL
roleset.ALERT = atspi.SPI_ROLE_ALERT
roleset.APPLICATION = atspi.SPI_ROLE_APPLICATION
roleset.BUTTON = atspi.SPI_ROLE_PUSH_BUTTON
roleset.CANVAS = atspi.SPI_ROLE_CANVAS
roleset.CHECK_BOX = atspi.SPI_ROLE_CHECK_BOX
roleset.CHECK_MENU_ITEM = atspi.SPI_ROLE_CHECK_MENU_ITEM
roleset.COMBO_BOX = atspi.SPI_ROLE_COMBO_BOX
roleset.DIALOG = atspi.SPI_ROLE_DIALOG
roleset.DRAWING_AREA = atspi.SPI_ROLE_DRAWING_AREA
roleset.EDITBAR = atspi.SPI_ROLE_EDITBAR
roleset.FILE_CHOOSER = atspi.SPI_ROLE_FILE_CHOOSER
roleset.FILLER = atspi.SPI_ROLE_FILLER
roleset.FRAME = atspi.SPI_ROLE_FRAME
roleset.ICON = atspi.SPI_ROLE_ICON
roleset.IMAGE = atspi.SPI_ROLE_IMAGE
roleset.LABEL = atspi.SPI_ROLE_LABEL
roleset.LIST = atspi.SPI_ROLE_LIST
roleset.LIST_ITEM = atspi.SPI_ROLE_LIST_ITEM
roleset.MENU = atspi.SPI_ROLE_MENU
roleset.MENU_BAR = atspi.SPI_ROLE_MENU_BAR
roleset.MENU_ITEM = atspi.SPI_ROLE_MENU_ITEM
roleset.PAGE_TAB = atspi.SPI_ROLE_PAGE_TAB
roleset.PAGE_TAB_LIST = atspi.SPI_ROLE_PAGE_TAB_LIST
roleset.PANEL = atspi.SPI_ROLE_PANEL
roleset.PASSWORD_TEXT = atspi.SPI_ROLE_PASSWORD_TEXT
roleset.POPUP_MENU = atspi.SPI_ROLE_POPUP_MENU
roleset.PROGRESS_BAR = atspi.SPI_ROLE_PROGRESS_BAR
roleset.RADIO_BUTTON = atspi.SPI_ROLE_RADIO_BUTTON
roleset.RADIO_MENU_ITEM = atspi.SPI_ROLE_RADIO_MENU_ITEM
roleset.SCROLL_BAR = atspi.SPI_ROLE_SCROLL_BAR
roleset.SCROLL_PANE = atspi.SPI_ROLE_SCROLL_PANE
roleset.SEPARATOR = atspi.SPI_ROLE_SEPARATOR
roleset.SLIDER = atspi.SPI_ROLE_SLIDER
roleset.SPIN_BUTTON = atspi.SPI_ROLE_SPIN_BUTTON
roleset.SPLIT_PANE = atspi.SPI_ROLE_SPLIT_PANE
roleset.STATUS_BAR = atspi.SPI_ROLE_STATUS_BAR
roleset.TABLE = atspi.SPI_ROLE_TABLE
roleset.TABLE_CELL = atspi.SPI_ROLE_TABLE_CELL
roleset.TABLE_COLUMN_HEADER = atspi.SPI_ROLE_TABLE_COLUMN_HEADER
roleset.TABLE_ROW_HEADER = atspi.SPI_ROLE_TABLE_ROW_HEADER
roleset.TEXT = atspi.SPI_ROLE_TEXT
roleset.TOGGLE_BUTTON = atspi.SPI_ROLE_TOGGLE_BUTTON
roleset.TOOL_BAR = atspi.SPI_ROLE_TOOL_BAR
roleset.TREE = atspi.SPI_ROLE_TREE
roleset.TREE_TABLE = atspi.SPI_ROLE_TREE_TABLE
roleset.UNKNOWN = atspi.SPI_ROLE_UNKNOWN
roleset.VIEWPORT = atspi.SPI_ROLE_VIEWPORT
roleset.WINDOW = atspi.SPI_ROLE_WINDOW

stateset = StateSet()
stateset.ACTIVE = atspi.SPI_STATE_ACTIVE
stateset.CHECKED = atspi.SPI_STATE_CHECKED
stateset.COLLAPSED = atspi.SPI_STATE_COLLAPSED
stateset.EDITABLE = atspi.SPI_STATE_EDITABLE
stateset.ENABLED = atspi.SPI_STATE_ENABLED
stateset.EXPANDABLE = atspi.SPI_STATE_EXPANDABLE
stateset.EXPANDED = atspi.SPI_STATE_EXPANDED
stateset.FOCUSABLE = atspi.SPI_STATE_FOCUSABLE
stateset.FOCUSED = atspi.SPI_STATE_FOCUSED
stateset.MULTILINE = atspi.SPI_STATE_MULTI_LINE
stateset.MULTISELECTABLE = atspi.SPI_STATE_MULTISELECTABLE
stateset.SELECTABLE = atspi.SPI_STATE_SELECTABLE
stateset.SELECTED = atspi.SPI_STATE_SELECTED
stateset.SENSITIVE = atspi.SPI_STATE_SENSITIVE
stateset.SHOWING = atspi.SPI_STATE_SHOWING
stateset.VISIBLE = atspi.SPI_STATE_VISIBLE

#
# Implement accessibility interface:
#
class PySpi(IAccessibility):
    '''
    An implementation of accessibility interface for Python bindings for
    AT-SPI (pyspi) library.
    '''
    name = "AT-SPI"
    actionset = actionset
    buttonset = buttonset
    keyset = keyset
    relationset = relationset
    roleset = roleset
    stateset = stateset

    def __init__(self):
        self._device = atspi.EventGenerator()

# Device:
    def mouseClick(self, x, y, button):
        self._device.click(x, y, button)

    def mouseDoubleClick(self, x, y, button):
        self._device.doubleClick(x, y, button)

    def mousePress(self, x, y, button):
        self._device.press(x, y, button)

    def mouseRelease(self, x, y, button):
        self._device.release(x, y, button)

    def mouseAbsoluteMotion(self, x, y):
        self._device.absoluteMotion(x, y)

    def mouseRelativeMotion(self, x, y):
        self._device.relativeMotion(x, y)

    def _keyboardEvent(self, keycode, modifiers):
        for modifier in modifiers:
            self._device.generateKeyboardEvent(modifier, '',
                                               atspi.SPI_KEY_PRESS)
        self._device.generateKeyboardEvent(keycode, '', atspi.SPI_KEY_SYM)
        for modifier in modifiers:
            self._device.generateKeyboardEvent(modifier, '',
                                               atspi.SPI_KEY_RELEASE)

# Object children:
    def getDesktop(self):
        try:
            return atspi.registry.getDesktop(_DESKTOP)
        except atspi.SpiException:
            return None

    def children(self, parent=None):
        if parent is None:
            parent = self.getDesktop()
        if parent is not None:
            try:
                i = 0
                while i < parent.getChildCount():
                    yield parent.getChildAtIndex(i)
                    i += 1
            except atspi.SpiException:
                pass

    def countChildren(self, parent=None):
        if parent is None:
            parent = self.getDesktop()
        try:
            return parent.getChildCount()
        except atspi.SpiException:
            return 0

    def _getChild(self, parent, index):
        if parent is None:
            parent = self.getDesktop()
        try:
            return parent.getChildAtIndex(index)
        except atspi.SpiException:
            return None

    def getParent(self, accessible):
        try:
            return accessible.getParent()
        except atspi.SpiException:
            return None

# Object properties:
    def getIndex(self, accessible):
        try:
            index = accessible.getIndexInParent()
            if index == -1 and self.getRole(accessible) == roleset.APPLICATION:
                name = self.getName(accessible)
                for i, app in enumerate(self.children()):
                    if name == self.getName(app):
                        index = i
                        break
            return index
        except atspi.SpiException:
            return -1

    @decodeResult()
    def getName(self, accessible):
        try:
            return accessible.getName()
        except atspi.SpiException:
            return None

    @decodeResult()
    def getDescription(self, accessible):
        try:
            return accessible.getDescription()
        except atspi.SpiException:
            return None

    def getRole(self, accessible):
        try:
            return accessible.getRole()
        except atspi.SpiException:
            return None

    def getPosition(self, accessible):
        try:
            component = accessible.getComponent()
            if component is None:
                return None
            return component.getExtents()[:2]
        except atspi.SpiException:
            return None

    def getSize(self, accessible):
        try:
            component = accessible.getComponent()
            if component is None:
                return None
            return component.getExtents()[2:]
        except atspi.SpiException:
            return None

    def getAttributes(self, accessible):
        return None

    @decodeResult()
    def getText(self, accessible):
        try:
            text = accessible.getText()
            if text is None:
                return None
            return text.getText(0, -1)
        except atspi.SpiException:
            return None

    @encodeLastArg()
    def setText(self, accessible, text):
        try:
            editabletext = accessible.getEditableText()
            if editabletext is None:
                return False
            if text is not None:
                editabletext.setTextContents(text)
                return True
        except atspi.SpiException:
            return False

    def getValue(self, accessible):
        try:
            value = accessible.getValue()
            if value is None:
                return None
            return value.getCurrentValue()
        except atspi.SpiException:
            return None

    def setValue(self, accessible, value):
        try:
            val = accessible.getValue()
            if val is None:
                return False
            val.setCurrentValue(value)
            return True
        except atspi.SpiException:
            return False

    def getImage(self, accessible):
        try:
            return accessible.getImage()
        except atspi.SpiException:
            return None

    def grabFocus(self, accessible):
        try:
            component = accessible.getComponent()
            if component is None:
                return False
            component.grabFocus()
            return True
        except atspi.SpiException:
            return False

# Object actions:
    def actions(self, accessible):
        try:
            action = accessible.getAction()
            if action is not None:
                for i in xrange(action.getNActions()):
                    yield action.getName(i)
        except atspi.SpiException:
            pass

    def doAction(self, accessible, action):
        name = action
        try:
            action = accessible.getAction()
            if action is None:
                return False
            num = None
            for i in xrange(action.getNActions()):
                if action.getName(i) == name:
                    num = i
                    break
            if num is None:
                return False
            return bool(action.doAction(num))
        except atspi.SpiException:
            return False

# Object relations:
    def relations(self, accessible):
        try:
            for relation in accessible.getRelationSet():
                yield relation.getRelationType()
        except atspi.SpiException:
            pass

    def relationTargets(self, accessible, relation):
        try:
            for rel in accessible.getRelationSet():
                if rel.getRelationType() == relation:
                    for i in xrange(rel.getNTargets()):
                        yield rel.getTarget(i)
                    break
        except atspi.SpiException:
            pass

# Object states:
    def states(self, accessible):
        try:
            states = accessible.getStateSet()
            if states is not None:
                return iter(states.states)
        except atspi.SpiException:
            pass
        return iter(())

    def inState(self, accessible, state):
        try:
            states = accessible.getStateSet()
            if states is None:
                return False
            return bool(states.contains(state))
        except atspi.SpiException:
            return False

