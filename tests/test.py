#!/usr/bin/python
'''

TODO:

x ApplySettings
x ChangePin
x Ping
x GetEntropy
x GetPublicKey
x GetAddress
x WipeDevice
x LoadDevice
x ResetDevice
x RecoveryDevice
x SignMessage
x VerifyMessage
x EstimateTxSize
- SignTx
x SimpleSignTx
- FirmwareErase
- FirmwareUpload

x protection levels
x neuspesna zmena pinu

pin backoff predelat pred zadanim pinu

- zrejme v sucinnosti s inymi testami
  x ButtonRequest/ButtonAck workflow
  x PinMatrixRequest/PinMatrixAck workflow
  x PassphraseRequest/PassphraseAck workflow

- rozsirit test_sign.tx o viac transakcii (zlozitejsich)
  x fee over threshold
  x not enough funds
  x viac ako jeden vstup a jeden vystup
  x iny cointype ako 0

- chceme v tomto release(?)
  x SignMessage workflow
  x VerifyMessage workflow

otestovat session handling (tento test bude zrejme failovat na RPi)
Failure_NotInitialized
Features reflects all variations of LoadDevice

x Zero signature test

x test bip39, utf, passphrase
x Clear session on ChangePin

Test s invalid adresou pro vystup
'''
