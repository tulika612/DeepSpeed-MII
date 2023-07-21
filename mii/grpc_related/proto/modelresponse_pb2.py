# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modelresponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13modelresponse.proto\x12\rmodelresponse\x1a\x1bgoogle/protobuf/empty.proto\"_\n\x05Value\x12\x10\n\x06svalue\x18\x01 \x01(\tH\x00\x12\x10\n\x06ivalue\x18\x02 \x01(\x03H\x00\x12\x10\n\x06\x66value\x18\x03 \x01(\x02H\x00\x12\x10\n\x06\x62value\x18\x04 \x01(\x08H\x00\x42\x0e\n\x0coneof_values\"\x1f\n\tSessionID\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\xed\x01\n\x13SingleStringRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12I\n\x0cquery_kwargs\x18\x02 \x03(\x0b\x32\x33.modelresponse.SingleStringRequest.QueryKwargsEntry\x12\x1c\n\x0f\x64\x65ployment_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\x42\x12\n\x10_deployment_name\"\xeb\x01\n\x12MultiStringRequest\x12\x0f\n\x07request\x18\x01 \x03(\t\x12H\n\x0cquery_kwargs\x18\x02 \x03(\x0b\x32\x32.modelresponse.MultiStringRequest.QueryKwargsEntry\x12\x1c\n\x0f\x64\x65ployment_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\x42\x12\n\x10_deployment_name\"\x85\x01\n\x11SingleStringReply\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x12\n\ntime_taken\x18\x02 \x01(\x02\x12\x18\n\x10model_time_taken\x18\x03 \x01(\x02\x12\x1c\n\x0f\x64\x65ployment_name\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_deployment_name\"\x84\x01\n\x10MultiStringReply\x12\x10\n\x08response\x18\x01 \x03(\t\x12\x12\n\ntime_taken\x18\x02 \x01(\x02\x12\x18\n\x10model_time_taken\x18\x03 \x01(\x02\x12\x1c\n\x0f\x64\x65ployment_name\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_deployment_name\"\xeb\x01\n\tQARequest\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\x12?\n\x0cquery_kwargs\x18\x03 \x03(\x0b\x32).modelresponse.QARequest.QueryKwargsEntry\x12\x1c\n\x0f\x64\x65ployment_name\x18\x04 \x01(\tH\x00\x88\x01\x01\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\x42\x12\n\x10_deployment_name\"\xd3\x02\n\x13\x43onversationRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1c\n\x0f\x63onversation_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x18\n\x10past_user_inputs\x18\x03 \x03(\t\x12\x1b\n\x13generated_responses\x18\x04 \x03(\t\x12I\n\x0cquery_kwargs\x18\x05 \x03(\x0b\x32\x33.modelresponse.ConversationRequest.QueryKwargsEntry\x12\x1c\n\x0f\x64\x65ployment_name\x18\x06 \x01(\tH\x01\x88\x01\x01\x1aH\n\x10QueryKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.modelresponse.Value:\x02\x38\x01\x42\x12\n\x10_conversation_idB\x12\n\x10_deployment_name\"\xc3\x01\n\x11\x43onversationReply\x12\x17\n\x0f\x63onversation_id\x18\x01 \x01(\x03\x12\x18\n\x10past_user_inputs\x18\x02 \x03(\t\x12\x1b\n\x13generated_responses\x18\x03 \x03(\t\x12\x12\n\ntime_taken\x18\x04 \x01(\x02\x12\x18\n\x10model_time_taken\x18\x05 \x01(\x02\x12\x1c\n\x0f\x64\x65ployment_name\x18\x06 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_deployment_name\"\xaf\x01\n\nImageReply\x12\x0e\n\x06images\x18\x01 \x03(\x0c\x12\x1d\n\x15nsfw_content_detected\x18\x02 \x03(\x08\x12\x0c\n\x04mode\x18\x03 \x01(\t\x12\x0e\n\x06size_w\x18\x04 \x01(\x03\x12\x0e\n\x06size_h\x18\x05 \x01(\x03\x12\x12\n\ntime_taken\x18\x06 \x01(\x02\x12\x1c\n\x0f\x64\x65ployment_name\x18\x07 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_deployment_name2\xd4\x06\n\rModelResponse\x12=\n\tTerminate\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x43\n\rCreateSession\x12\x18.modelresponse.SessionID\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x0e\x44\x65stroySession\x12\x18.modelresponse.SessionID\x1a\x16.google.protobuf.Empty\"\x00\x12V\n\x0eGeneratorReply\x12!.modelresponse.MultiStringRequest\x1a\x1f.modelresponse.MultiStringReply\"\x00\x12]\n\x13\x43lassificationReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12V\n\x16QuestionAndAnswerReply\x12\x18.modelresponse.QARequest\x1a .modelresponse.SingleStringReply\"\x00\x12W\n\rFillMaskReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12\x62\n\x18TokenClassificationReply\x12\".modelresponse.SingleStringRequest\x1a .modelresponse.SingleStringReply\"\x00\x12]\n\x13\x43onversationalReply\x12\".modelresponse.ConversationRequest\x1a .modelresponse.ConversationReply\"\x00\x12N\n\x0cTxt2ImgReply\x12!.modelresponse.MultiStringRequest\x1a\x19.modelresponse.ImageReply\"\x00\x32Y\n\x14\x44\x65ploymentManagement\x12\x41\n\rAddDeployment\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'modelresponse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._options = None
  _SINGLESTRINGREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
  _MULTISTRINGREQUEST_QUERYKWARGSENTRY._options = None
  _MULTISTRINGREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
  _QAREQUEST_QUERYKWARGSENTRY._options = None
  _QAREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
  _CONVERSATIONREQUEST_QUERYKWARGSENTRY._options = None
  _CONVERSATIONREQUEST_QUERYKWARGSENTRY._serialized_options = b'8\001'
  _globals['_VALUE']._serialized_start=67
  _globals['_VALUE']._serialized_end=162
  _globals['_SESSIONID']._serialized_start=164
  _globals['_SESSIONID']._serialized_end=195
  _globals['_SINGLESTRINGREQUEST']._serialized_start=198
  _globals['_SINGLESTRINGREQUEST']._serialized_end=435
  _globals['_SINGLESTRINGREQUEST_QUERYKWARGSENTRY']._serialized_start=343
  _globals['_SINGLESTRINGREQUEST_QUERYKWARGSENTRY']._serialized_end=415
  _globals['_MULTISTRINGREQUEST']._serialized_start=438
  _globals['_MULTISTRINGREQUEST']._serialized_end=673
  _globals['_MULTISTRINGREQUEST_QUERYKWARGSENTRY']._serialized_start=343
  _globals['_MULTISTRINGREQUEST_QUERYKWARGSENTRY']._serialized_end=415
  _globals['_SINGLESTRINGREPLY']._serialized_start=676
  _globals['_SINGLESTRINGREPLY']._serialized_end=809
  _globals['_MULTISTRINGREPLY']._serialized_start=812
  _globals['_MULTISTRINGREPLY']._serialized_end=944
  _globals['_QAREQUEST']._serialized_start=947
  _globals['_QAREQUEST']._serialized_end=1182
  _globals['_QAREQUEST_QUERYKWARGSENTRY']._serialized_start=343
  _globals['_QAREQUEST_QUERYKWARGSENTRY']._serialized_end=415
  _globals['_CONVERSATIONREQUEST']._serialized_start=1185
  _globals['_CONVERSATIONREQUEST']._serialized_end=1524
  _globals['_CONVERSATIONREQUEST_QUERYKWARGSENTRY']._serialized_start=343
  _globals['_CONVERSATIONREQUEST_QUERYKWARGSENTRY']._serialized_end=415
  _globals['_CONVERSATIONREPLY']._serialized_start=1527
  _globals['_CONVERSATIONREPLY']._serialized_end=1722
  _globals['_IMAGEREPLY']._serialized_start=1725
  _globals['_IMAGEREPLY']._serialized_end=1900
  _globals['_MODELRESPONSE']._serialized_start=1903
  _globals['_MODELRESPONSE']._serialized_end=2755
  _globals['_DEPLOYMENTMANAGEMENT']._serialized_start=2757
  _globals['_DEPLOYMENTMANAGEMENT']._serialized_end=2846
# @@protoc_insertion_point(module_scope)
