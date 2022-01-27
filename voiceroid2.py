import pywinauto
import subprocess


class Voicerid2:
    def __init__(self):
        parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
        # app = pywinauto.Application().connect(path="cmd.exe")
        # self.console = app.window()

        self.voiceroid2 = self.__search_child_byname(
            "VOICEROID2", parentUIAElement)
        if not self.voiceroid2:
            self.voiceroid2 = self.__search_child_byname(
                "VOICEROID2*", parentUIAElement)

        # text box
        textEditViewEle = self.__search_child_byclassname(
            "TextEditView", self.voiceroid2)
        textBoxEle = self.__search_child_byclassname(
            "TextBox", textEditViewEle)
        self.textbox = pywinauto.controls.uia_controls.EditWrapper(textBoxEle)

        # buttons
        buttons = self.__search_child_byclassname(
            "Button", textEditViewEle, target_all=True)
        for button in buttons:
            textBlockEle = self.__search_child_byclassname("TextBlock", button)
            if textBlockEle.name == "再生":
                self.playButton = pywinauto.controls.uia_controls.ButtonWrapper(
                    button)

    def edit_text(self, text):
        self.textbox.set_edit_text(text)

    def speak(self, text=""):
        if text:
            self.edit_text(text)
        self.playButton.click()
        # self.console.set_focus()

    def __search_child_byname(self, name, uiaElementInfo):
        for childElement in uiaElementInfo.children():
            if childElement.name == name:
                return childElement
        return False

    def __search_child_byclassname(self, class_name, uiaElementInfo, target_all=False):
        target = []
        for childElement in uiaElementInfo.children():
            if childElement.class_name == class_name:
                if target_all == False:
                    return childElement
                else:
                    target.append(childElement)
        if target_all == False:
            return False
        else:
            return target


if __name__ == "__main__":
    voiceroid2 = Voicerid2()
    while(True):
        print(" > ", end="")
        text = input()
        if text == 'q':
            break
        voiceroid2.speak(text)
