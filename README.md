# PythonCodeResearch

### Emacs as Python IDE
- config file in .emacs.d/init.el
```
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))

(package-initialize)
(elpy-enable)
```
- `M-x list-packages RET`
- `M-x package-install RET elpy RET`
