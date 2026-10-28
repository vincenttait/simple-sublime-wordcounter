import re
import sublime
import sublime_plugin

class WordCountListener(sublime_plugin.EventListener):
    def update(self, view):
        sels = [s for s in view.sel() if not s.empty()]
        region_text = " ".join(view.substr(s) for s in sels) if sels \
            else view.substr(sublime.Region(0, view.size()))
        words = len(re.findall(r"\S+", region_text))
        view.set_status("wordcount", "{} words".format(words))

    def on_selection_modified_async(self, view):
        self.update(view)

    def on_activated_async(self, view):
        self.update(view)
