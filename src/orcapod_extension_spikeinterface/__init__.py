"""OrcaPod extension for SpikeInterface types (ITL-473).

Provides ``LogicalSIRecording``, ``LogicalSISorting``, ``LogicalSIMotion``,
``LogicalSISortingAnalyzer`` and their corresponding semantic hashers as
first-class orcapod value types.

Register via the normalized extension API::

    import orcapod as op
    from orcapod_extension_spikeinterface import spikeinterface_extension
    op.register_extension(spikeinterface_extension)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ._spikeinterface_types import (
    LogicalSIRecording,
    LogicalSISorting,
    LogicalSIMotion,
    LogicalSISortingAnalyzer,
    SIRecordingHandler,
    SISortingHandler,
    SIMotionHandler,
    SISortingAnalyzerHandler,
    _register_spikeinterface_types,
)

if TYPE_CHECKING:
    from orcapod.contexts import DataContext

__all__ = [
    "SpikeInterfaceExtension",
    "spikeinterface_extension",
    "LogicalSIRecording",
    "LogicalSISorting",
    "LogicalSIMotion",
    "LogicalSISortingAnalyzer",
    "SIRecordingHandler",
    "SISortingHandler",
    "SIMotionHandler",
    "SISortingAnalyzerHandler",
]


class SpikeInterfaceExtension:
    """OrcaPod extension object for SpikeInterface types.

    Implements ``orcapod.OrcapodExtension``. The canonical way to use this
    extension is via the module-level ``spikeinterface_extension`` singleton::

        import orcapod as op
        from orcapod_extension_spikeinterface import spikeinterface_extension
        op.register_extension(spikeinterface_extension)

    Attributes:
        name: Extension identifier (``"spikeinterface"``).
    """

    name = "spikeinterface"

    def register(self, context: DataContext) -> None:
        """Register all SpikeInterface types into ``context``.

        Registers ``LogicalSIRecording``, ``LogicalSISorting``,
        ``LogicalSIMotion``, ``LogicalSISortingAnalyzer`` and their handlers.
        Idempotent — safe to call multiple times on the same context.

        Args:
            context: Target ``DataContext``. Always a concrete context —
                resolution from ``None`` is handled by ``op.register_extension``.
        """
        _register_spikeinterface_types(context)


#: Module-level singleton — the canonical extension object.
#: Pass to ``op.register_extension()`` to wire SI types into a context.
spikeinterface_extension = SpikeInterfaceExtension()
