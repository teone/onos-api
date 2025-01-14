# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/kpimon/kpimon.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterator, Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class GetRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetResponse(betterproto.Message):
    measurements: Dict[str, "MeasurementItems"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass(eq=False, repr=False)
class MeasurementItems(betterproto.Message):
    measurement_items: List["MeasurementItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MeasurementItem(betterproto.Message):
    measurement_records: List["MeasurementRecord"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class IntegerValue(betterproto.Message):
    value: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class RealValue(betterproto.Message):
    value: float = betterproto.double_field(1)


@dataclass(eq=False, repr=False)
class NoValue(betterproto.Message):
    value: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class MeasurementRecord(betterproto.Message):
    timestamp: int = betterproto.uint64_field(2)
    measurement_name: str = betterproto.string_field(3)
    measurement_value: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(4)
    )


class KpimonStub(betterproto.ServiceStub):
    async def list_measurements(self) -> "GetResponse":

        request = GetRequest()

        return await self._unary_unary(
            "/onos.kpimon.Kpimon/ListMeasurements", request, GetResponse
        )

    async def watch_measurements(self) -> AsyncIterator["GetResponse"]:

        request = GetRequest()

        async for response in self._unary_stream(
            "/onos.kpimon.Kpimon/WatchMeasurements",
            request,
            GetResponse,
        ):
            yield response


class KpimonBase(ServiceBase):
    async def list_measurements(self) -> "GetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_measurements(self) -> AsyncIterator["GetResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_list_measurements(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.list_measurements(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_watch_measurements(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        await self._call_rpc_handler_server_stream(
            self.watch_measurements,
            stream,
            request_kwargs,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/onos.kpimon.Kpimon/ListMeasurements": grpclib.const.Handler(
                self.__rpc_list_measurements,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetRequest,
                GetResponse,
            ),
            "/onos.kpimon.Kpimon/WatchMeasurements": grpclib.const.Handler(
                self.__rpc_watch_measurements,
                grpclib.const.Cardinality.UNARY_STREAM,
                GetRequest,
                GetResponse,
            ),
        }


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
