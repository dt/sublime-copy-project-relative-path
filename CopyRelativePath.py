# Copyright 2014 Foursquare Labs Inc. All Rights Reserved.

import os
import sublime, sublime_plugin

class CopyProjectRelativePathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    cur = self.view.file_name() or ''
    proj = sublime.active_window().project_file_name() or ''
    root = os.path.dirname(proj)
    rel = os.path.relpath(cur, root)
    if rel:
      print('Copied "{}" to clipboard'.format(rel))
      sublime.set_clipboard(rel)
