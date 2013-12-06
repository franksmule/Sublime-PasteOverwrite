import sublime, sublime_plugin  
  
class PasteinsertCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        the_sels = self.view.sel()
        for a_sel in the_sels:
            he_text = self.view.substr(a_sel)
            copylen = len(sublime.get_clipboard())
            self.view.insert(edit, a_sel.begin(), sublime.get_clipboard())
            self.view.replace(edit,a_sel,"")
            eraseRegion = sublime.Region(a_sel.end() + copylen, a_sel.end() + copylen*2)
            self.view.erase(edit, eraseRegion)