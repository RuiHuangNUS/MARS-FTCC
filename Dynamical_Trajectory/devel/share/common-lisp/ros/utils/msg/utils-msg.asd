
(cl:in-package :asdf)

(defsystem "utils-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "debug" :depends-on ("_package_debug"))
    (:file "_package_debug" :depends-on ("_package"))
  ))