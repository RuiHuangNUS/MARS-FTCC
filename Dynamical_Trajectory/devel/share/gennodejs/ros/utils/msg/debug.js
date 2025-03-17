// Auto-generated. Do not edit!

// (in-package utils.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class debug {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.operation_type = null;
      this.id1 = null;
      this.id2 = null;
      this.id3 = null;
      this.data1 = null;
      this.data2 = null;
      this.data3 = null;
      this.data4 = null;
      this.data5 = null;
      this.data6 = null;
      this.data7 = null;
      this.data8 = null;
    }
    else {
      if (initObj.hasOwnProperty('operation_type')) {
        this.operation_type = initObj.operation_type
      }
      else {
        this.operation_type = 0;
      }
      if (initObj.hasOwnProperty('id1')) {
        this.id1 = initObj.id1
      }
      else {
        this.id1 = 0;
      }
      if (initObj.hasOwnProperty('id2')) {
        this.id2 = initObj.id2
      }
      else {
        this.id2 = 0;
      }
      if (initObj.hasOwnProperty('id3')) {
        this.id3 = initObj.id3
      }
      else {
        this.id3 = 0;
      }
      if (initObj.hasOwnProperty('data1')) {
        this.data1 = initObj.data1
      }
      else {
        this.data1 = 0.0;
      }
      if (initObj.hasOwnProperty('data2')) {
        this.data2 = initObj.data2
      }
      else {
        this.data2 = 0.0;
      }
      if (initObj.hasOwnProperty('data3')) {
        this.data3 = initObj.data3
      }
      else {
        this.data3 = 0.0;
      }
      if (initObj.hasOwnProperty('data4')) {
        this.data4 = initObj.data4
      }
      else {
        this.data4 = 0.0;
      }
      if (initObj.hasOwnProperty('data5')) {
        this.data5 = initObj.data5
      }
      else {
        this.data5 = 0.0;
      }
      if (initObj.hasOwnProperty('data6')) {
        this.data6 = initObj.data6
      }
      else {
        this.data6 = 0.0;
      }
      if (initObj.hasOwnProperty('data7')) {
        this.data7 = initObj.data7
      }
      else {
        this.data7 = 0.0;
      }
      if (initObj.hasOwnProperty('data8')) {
        this.data8 = initObj.data8
      }
      else {
        this.data8 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type debug
    // Serialize message field [operation_type]
    bufferOffset = _serializer.uint8(obj.operation_type, buffer, bufferOffset);
    // Serialize message field [id1]
    bufferOffset = _serializer.int32(obj.id1, buffer, bufferOffset);
    // Serialize message field [id2]
    bufferOffset = _serializer.int32(obj.id2, buffer, bufferOffset);
    // Serialize message field [id3]
    bufferOffset = _serializer.int32(obj.id3, buffer, bufferOffset);
    // Serialize message field [data1]
    bufferOffset = _serializer.float64(obj.data1, buffer, bufferOffset);
    // Serialize message field [data2]
    bufferOffset = _serializer.float64(obj.data2, buffer, bufferOffset);
    // Serialize message field [data3]
    bufferOffset = _serializer.float64(obj.data3, buffer, bufferOffset);
    // Serialize message field [data4]
    bufferOffset = _serializer.float64(obj.data4, buffer, bufferOffset);
    // Serialize message field [data5]
    bufferOffset = _serializer.float64(obj.data5, buffer, bufferOffset);
    // Serialize message field [data6]
    bufferOffset = _serializer.float64(obj.data6, buffer, bufferOffset);
    // Serialize message field [data7]
    bufferOffset = _serializer.float64(obj.data7, buffer, bufferOffset);
    // Serialize message field [data8]
    bufferOffset = _serializer.float64(obj.data8, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type debug
    let len;
    let data = new debug(null);
    // Deserialize message field [operation_type]
    data.operation_type = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [id1]
    data.id1 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [id2]
    data.id2 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [id3]
    data.id3 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [data1]
    data.data1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data2]
    data.data2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data3]
    data.data3 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data4]
    data.data4 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data5]
    data.data5 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data6]
    data.data6 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data7]
    data.data7 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [data8]
    data.data8 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 77;
  }

  static datatype() {
    // Returns string type for a message object
    return 'utils/debug';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0cfc85dbf6535c56acc25a584f5c9d9d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 operation_type #debug 操作类型
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new debug(null);
    if (msg.operation_type !== undefined) {
      resolved.operation_type = msg.operation_type;
    }
    else {
      resolved.operation_type = 0
    }

    if (msg.id1 !== undefined) {
      resolved.id1 = msg.id1;
    }
    else {
      resolved.id1 = 0
    }

    if (msg.id2 !== undefined) {
      resolved.id2 = msg.id2;
    }
    else {
      resolved.id2 = 0
    }

    if (msg.id3 !== undefined) {
      resolved.id3 = msg.id3;
    }
    else {
      resolved.id3 = 0
    }

    if (msg.data1 !== undefined) {
      resolved.data1 = msg.data1;
    }
    else {
      resolved.data1 = 0.0
    }

    if (msg.data2 !== undefined) {
      resolved.data2 = msg.data2;
    }
    else {
      resolved.data2 = 0.0
    }

    if (msg.data3 !== undefined) {
      resolved.data3 = msg.data3;
    }
    else {
      resolved.data3 = 0.0
    }

    if (msg.data4 !== undefined) {
      resolved.data4 = msg.data4;
    }
    else {
      resolved.data4 = 0.0
    }

    if (msg.data5 !== undefined) {
      resolved.data5 = msg.data5;
    }
    else {
      resolved.data5 = 0.0
    }

    if (msg.data6 !== undefined) {
      resolved.data6 = msg.data6;
    }
    else {
      resolved.data6 = 0.0
    }

    if (msg.data7 !== undefined) {
      resolved.data7 = msg.data7;
    }
    else {
      resolved.data7 = 0.0
    }

    if (msg.data8 !== undefined) {
      resolved.data8 = msg.data8;
    }
    else {
      resolved.data8 = 0.0
    }

    return resolved;
    }
};

module.exports = debug;
