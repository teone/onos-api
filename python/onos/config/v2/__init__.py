# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/config/v2/configuration.proto, onos/config/v2/transaction.proto, onos/config/v2/value.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class ValueType(betterproto.Enum):
    """ValueType is the type for a value"""

    EMPTY = 0
    STRING = 1
    INT = 2
    UINT = 3
    BOOL = 4
    DECIMAL = 5
    FLOAT = 6
    BYTES = 7
    LEAFLIST_STRING = 8
    LEAFLIST_INT = 9
    LEAFLIST_UINT = 10
    LEAFLIST_BOOL = 11
    LEAFLIST_DECIMAL = 12
    LEAFLIST_FLOAT = 13
    LEAFLIST_BYTES = 14


class ConfigurationState(betterproto.Enum):
    """
    ConfigurationState is the configuration state of a configuration phase
    """

    # CONFIGURATION_PENDING indicates the configuration is PENDING
    CONFIGURATION_PENDING = 0
    # COMPLETE indicates the configuration is COMPLETE
    CONFIGURATION_COMPLETE = 2


class ConfigurationEventType(betterproto.Enum):
    """
    ConfigurationEventType configuration event types for configuration store
    """

    # CONFIGURATION_EVENT_UNKNOWN indicates unknown configuration store event
    CONFIGURATION_EVENT_UNKNOWN = 0
    # CONFIGURATION_CREATED indicates the configuration entry in the store is
    # created
    CONFIGURATION_CREATED = 1
    # CONFIGURATION_UPDATED indicates the configuration entry in the store is
    # updated
    CONFIGURATION_UPDATED = 2
    # CONFIGURATION_DELETED indicates the configuration entry in the store is
    # deleted
    CONFIGURATION_DELETED = 3
    # CONFIGURATION_REPLAYED
    CONFIGURATION_REPLAYED = 4


class TransactionState(betterproto.Enum):
    """TransactionState is the transaction state of a transaction phase"""

    # TRANSACTION_PENDING indicates the transaction is pending
    TRANSACTION_PENDING = 0
    # TRANSACTION_COMPLETE indicates the transaction is complete
    TRANSACTION_COMPLETE = 2
    # TRANSACTION_FAILED indicates the transaction failed
    TRANSACTION_FAILED = 3
    # TRANSACTION_VALIDATING indicates the transaction is in the validating state
    TRANSACTION_VALIDATING = 4
    # TRANSACTION_VALIDATED indicates the transaction is validated successfully
    TRANSACTION_VALIDATED = 5
    # TRANSACTION_VALIDATION_FAILED indicates the transaction validation is
    # failed
    TRANSACTION_VALIDATION_FAILED = 6


class TransactionPhase(betterproto.Enum):
    """TransactionPhase is the phase of a Transaction"""

    # TRANSACTION_CHANGE indicates the transaction has been requested
    TRANSACTION_CHANGE = 0
    # TRANSACTION_ROLLBACK indicates a rollback has been requested for the
    # transaction
    TRANSACTION_ROLLBACK = 1


class TransactionEventType(betterproto.Enum):
    """TransactionEventType transaction event types for transaction store"""

    TRANSACTION_EVENT_UNKNOWN = 0
    TRANSACTION_CREATED = 1
    TRANSACTION_UPDATED = 2
    TRANSACTION_DELETED = 3
    TRANSACTION_REPLAYED = 4


@dataclass(eq=False, repr=False)
class TypedValue(betterproto.Message):
    """TypedValue is a value represented as a byte array"""

    # 'bytes' is the bytes array
    bytes_: bytes = betterproto.bytes_field(1)
    # 'type' is the value type
    type: "ValueType" = betterproto.enum_field(2)
    # 'type_opts' is a set of type options
    type_opts: List[int] = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class PathValue(betterproto.Message):
    """PathValue is an individual Path/Value combination"""

    # 'path' is the path to change
    path: str = betterproto.string_field(1)
    # 'value' is the change value
    value: "TypedValue" = betterproto.message_field(2)
    # 'removed' indicates whether this is a delete
    removed: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class Configuration(betterproto.Message):
    """Configuration represents complete desired target configuration"""

    # 'id' is a unique configuration identifier
    id: str = betterproto.string_field(1)
    # 'target_id' is the target to which the desired target configuration applies
    target_id: str = betterproto.string_field(2)
    # 'target_version' is the version to which desired target configuration
    # applies
    target_version: str = betterproto.string_field(3)
    # 'target_type' is an optional target type to which to apply this desired
    # target configuration
    target_type: str = betterproto.string_field(4)
    # 'values' is a map of path/values to set
    values: Dict[str, "PathValue"] = betterproto.map_field(
        5, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    # 'ConfigurationStatus' is the current lifecycle status of the configuration
    status: "ConfigurationStatus" = betterproto.message_field(6)
    # revision is configuration revision
    revision: int = betterproto.uint64_field(7)


@dataclass(eq=False, repr=False)
class ConfigurationStatus(betterproto.Message):
    """ConfigurationStatus is the status of a Configuration"""

    # 'state' is the state of the transaction within a Phase
    state: "ConfigurationState" = betterproto.enum_field(1)
    # mastershipState mastership info
    mastership_state: "MastershipState" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MastershipState(betterproto.Message):
    """Mastership state"""

    term: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class ConfigurationEvent(betterproto.Message):
    """ConfigurationEvent configuration store event"""

    # ConfigurationEventType configuration event type
    type: "ConfigurationEventType" = betterproto.enum_field(1)
    configuration: "Configuration" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Transaction(betterproto.Message):
    """Transaction refers to a multi-target transactional change"""

    # 'id' is the unique identifier of the transaction This field should be set
    # prior to persisting the object.
    id: str = betterproto.string_field(1)
    # 'index' is a monotonically increasing, globally unique index of the change
    # The index is provided by the store, is static and unique for each unique
    # change identifier, and should not be modified by client code.
    index: int = betterproto.uint64_field(2)
    # 'revision' is the change revision number The revision number is provided by
    # the store and should not be modified by client code. Each unique state of
    # the change will be assigned a unique revision number which can be used for
    # optimistic concurrency control when updating or deleting the change state.
    revision: int = betterproto.uint64_field(3)
    # 'status' is the current lifecycle status of the transaction
    status: "TransactionStatus" = betterproto.message_field(4)
    # 'created' is the time at which the transaction was created
    created: datetime = betterproto.message_field(5)
    # 'updated' is the time at which the transaction was last updated
    updated: datetime = betterproto.message_field(6)
    # 'changes' is a set of changes to apply to targets The list of changes
    # should contain only a single change per target/version pair.
    changes: List["Change"] = betterproto.message_field(7)
    # 'deleted' is a flag indicating whether this transaction is being deleted by
    # a snapshot
    deleted: bool = betterproto.bool_field(8)
    # 'dependency' is a reference to the transaction on which this transaction is
    # dependent
    dependency: "TransactionRef" = betterproto.message_field(9)
    # 'dependents' is a list of references to transactions that depend on this
    # transaction
    dependents: List["TransactionRef"] = betterproto.message_field(10)
    # 'username' is the name of the user that made the transaction
    username: str = betterproto.string_field(11)


@dataclass(eq=False, repr=False)
class TransactionRef(betterproto.Message):
    """TransactionRef is a reference to a transaction"""

    none: "betterproto_lib_google_protobuf.Empty" = betterproto.message_field(
        1, group="id"
    )
    transaction_id: str = betterproto.string_field(2, group="id")


@dataclass(eq=False, repr=False)
class Change(betterproto.Message):
    """Change represents a configuration change to a single target"""

    # 'target_id' is the identifier of the target to which this change applies
    target_id: str = betterproto.string_field(1)
    # 'target_version' is an optional target version to which to apply this
    # change
    target_version: str = betterproto.string_field(2)
    # 'target_type' is an optional target type to which to apply this change
    target_type: str = betterproto.string_field(3)
    # 'values' is a set of change values to apply
    values: List["ChangeValue"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ChangeValue(betterproto.Message):
    """
    ChangeValue is an individual Path/Value and removed flag combination in a
    Change
    """

    # 'path' is the path to change
    path: str = betterproto.string_field(1)
    # 'value' is the change value
    value: "TypedValue" = betterproto.message_field(2)
    # 'removed' indicates whether this is a delete
    removed: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class TransactionStatus(betterproto.Message):
    """TransactionStatus is the status of a Transaction"""

    # 'phase' is the current phase of the
    phase: "TransactionPhase" = betterproto.enum_field(1)
    # 'state' is the state of the transaction within a Phase
    state: "TransactionState" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class TransactionEvent(betterproto.Message):
    """TransactionEvent transaction store event"""

    type: "TransactionEventType" = betterproto.enum_field(1)
    transaction: "Transaction" = betterproto.message_field(2)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
