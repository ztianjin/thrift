class TType:
  STOP   = 0
  VOID   = 1
  BOOL   = 2
  BYTE   = 3
  I08    = 3
  DOUBLE = 4
  I16    = 6
  I32    = 8
  I64    = 10
  STRING = 11
  UTF7   = 11
  STRUCT = 12
  MAP    = 13
  SET    = 14
  LIST   = 15
  UTF8   = 16
  UTF16  = 17

class TMessageType:
  CALL  = 1
  REPLY = 2

class TProtocolBase:

  """Base class for Thrift protocol driver."""

  def __init__(self, itrans, otrans=None):
    self.itrans = self.otrans = itrans
    if otrans != None:
      self.otrans = otrans

  def writeMessageBegin(self, name, type, seqid):
    pass

  def writeMessageEnd(self):
    pass

  def writeStructBegin(self, name):
    pass

  def writeStructEnd(self):
    pass

  def writeFieldBegin(self, name, type, id):
    pass

  def writeFieldEnd(self):
    pass

  def writeFieldStop(self):
    pass

  def writeMapBegin(self, ktype, vtype, size):
    pass

  def writeMapEnd(self):
    pass

  def writeListBegin(self, etype, size):
    pass

  def writeListEnd(self):
    pass

  def writeSetBegin(self, etype, size):
    pass

  def writeSetEnd(self):
    pass

  def writeBool(self, bool):
    pass

  def writeByte(self, byte):
    pass

  def writeI16(self, i16):
    pass

  def writeI32(self, i32):
    pass

  def writeI64(self, i64):
    pass

  def writeDouble(self, dub):
    pass

  def writeString(self, str):
    pass

  def readMessageBegin(self):
    pass

  def readMessageEnd(self):
    pass

  def readStructBegin(self):
    pass

  def readStructEnd(self):
    pass

  def readFieldBegin(self):
    pass

  def readFieldEnd(self):
    pass

  def readMapBegin(self):
    pass

  def readMapEnd(self):
    pass

  def readListBegin(self):
    pass

  def readListEnd(self):
    pass

  def readSetBegin(self):
    pass

  def readSetEnd(self):
    pass

  def readBool(self):
    pass

  def readByte(self):
    pass

  def readI16(self):
    pass

  def readI32(self):
    pass

  def readI64(self):
    pass

  def readDouble(self):
    pass

  def readString(self):
    pass

  def skip(self, type):
    if type == TType.STOP:
      return
    elif type == TType.BOOL:
      self.readBool()
    elif type == TType.BYTE:
      self.readByte()
    elif type == TType.I16:
      self.readI16()
    elif type == TType.I32:
      self.readI32()
    elif type == TType.I64:
      self.readI64()
    elif type == TType.DOUBLE:
      self.readDouble()
    elif type == TType.STRING:
      self.readString()
    elif type == TType.STRUCT:
      name = self.readStructBegin()
      while True:
        (name, type, id) = self.readFieldBegin()
        if type == TType.STOP:
          break
        self.skip(type)
        self.readFieldEnd()
      self.readStructEnd()
    elif type == TType.MAP:
      (ktype, vtype, size) = self.readMapBegin()
      for i in range(size):
        self.skip(ktype)
        self.skip(vtype)
      self.readMapEnd()
    elif type == TType.SET:
      (etype, size) = self.readSetBegin()
      for i in range(size):
        self.skip(etype)
      self.readSetEnd()
    elif type == TType.LIST:
      (etype, size) = self.readListBegin()
      for i in range(size):
        self.skip(etype)
      self.readListEnd()

class TProtocolFactory:
  def getIOProtocols(self, itrans, otrans):
    pass