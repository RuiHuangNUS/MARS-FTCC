;; Auto-generated. Do not edit!


(when (boundp 'utils::debug)
  (if (not (find-package "UTILS"))
    (make-package "UTILS"))
  (shadow 'debug (find-package "UTILS")))
(unless (find-package "UTILS::DEBUG")
  (make-package "UTILS::DEBUG"))

(in-package "ROS")
;;//! \htmlinclude debug.msg.html


(defclass utils::debug
  :super ros::object
  :slots (_operation_type _id1 _id2 _id3 _data1 _data2 _data3 _data4 _data5 _data6 _data7 _data8 ))

(defmethod utils::debug
  (:init
   (&key
    ((:operation_type __operation_type) 0)
    ((:id1 __id1) 0)
    ((:id2 __id2) 0)
    ((:id3 __id3) 0)
    ((:data1 __data1) 0.0)
    ((:data2 __data2) 0.0)
    ((:data3 __data3) 0.0)
    ((:data4 __data4) 0.0)
    ((:data5 __data5) 0.0)
    ((:data6 __data6) 0.0)
    ((:data7 __data7) 0.0)
    ((:data8 __data8) 0.0)
    )
   (send-super :init)
   (setq _operation_type (round __operation_type))
   (setq _id1 (round __id1))
   (setq _id2 (round __id2))
   (setq _id3 (round __id3))
   (setq _data1 (float __data1))
   (setq _data2 (float __data2))
   (setq _data3 (float __data3))
   (setq _data4 (float __data4))
   (setq _data5 (float __data5))
   (setq _data6 (float __data6))
   (setq _data7 (float __data7))
   (setq _data8 (float __data8))
   self)
  (:operation_type
   (&optional __operation_type)
   (if __operation_type (setq _operation_type __operation_type)) _operation_type)
  (:id1
   (&optional __id1)
   (if __id1 (setq _id1 __id1)) _id1)
  (:id2
   (&optional __id2)
   (if __id2 (setq _id2 __id2)) _id2)
  (:id3
   (&optional __id3)
   (if __id3 (setq _id3 __id3)) _id3)
  (:data1
   (&optional __data1)
   (if __data1 (setq _data1 __data1)) _data1)
  (:data2
   (&optional __data2)
   (if __data2 (setq _data2 __data2)) _data2)
  (:data3
   (&optional __data3)
   (if __data3 (setq _data3 __data3)) _data3)
  (:data4
   (&optional __data4)
   (if __data4 (setq _data4 __data4)) _data4)
  (:data5
   (&optional __data5)
   (if __data5 (setq _data5 __data5)) _data5)
  (:data6
   (&optional __data6)
   (if __data6 (setq _data6 __data6)) _data6)
  (:data7
   (&optional __data7)
   (if __data7 (setq _data7 __data7)) _data7)
  (:data8
   (&optional __data8)
   (if __data8 (setq _data8 __data8)) _data8)
  (:serialization-length
   ()
   (+
    ;; uint8 _operation_type
    1
    ;; int32 _id1
    4
    ;; int32 _id2
    4
    ;; int32 _id3
    4
    ;; float64 _data1
    8
    ;; float64 _data2
    8
    ;; float64 _data3
    8
    ;; float64 _data4
    8
    ;; float64 _data5
    8
    ;; float64 _data6
    8
    ;; float64 _data7
    8
    ;; float64 _data8
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _operation_type
       (write-byte _operation_type s)
     ;; int32 _id1
       (write-long _id1 s)
     ;; int32 _id2
       (write-long _id2 s)
     ;; int32 _id3
       (write-long _id3 s)
     ;; float64 _data1
       (sys::poke _data1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data2
       (sys::poke _data2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data3
       (sys::poke _data3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data4
       (sys::poke _data4 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data5
       (sys::poke _data5 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data6
       (sys::poke _data6 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data7
       (sys::poke _data7 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _data8
       (sys::poke _data8 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _operation_type
     (setq _operation_type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int32 _id1
     (setq _id1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _id2
     (setq _id2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _id3
     (setq _id3 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _data1
     (setq _data1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data2
     (setq _data2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data3
     (setq _data3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data4
     (setq _data4 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data5
     (setq _data5 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data6
     (setq _data6 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data7
     (setq _data7 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _data8
     (setq _data8 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get utils::debug :md5sum-) "0cfc85dbf6535c56acc25a584f5c9d9d")
(setf (get utils::debug :datatype-) "utils/debug")
(setf (get utils::debug :definition-)
      "uint8 operation_type #debug 操作类型
int32 id1            #具体行为
int32 id2
int32 id3
float64 data1
float64 data2
float64 data3
float64 data4
float64 data5
float64 data6
float64 data7
float64 data8

")



(provide :utils/debug "0cfc85dbf6535c56acc25a584f5c9d9d")


