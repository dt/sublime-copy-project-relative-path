# Copyright 2014 Foursquare Labs Inc. All Rights Reserved.

import os
import sublime, sublime_plugin

class CopyRelativePathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    cur = self.view.file_name() or ''
    proj = sublime.active_window().project_file_name() or ''
    root = os.path.join(os.path.dirname(proj), '')
    rel = cur.replace(root, '')
    if rel:
      print('Copied "{}" to clipboard'.format(rel))
      sublime.set_clipboard(rel)
