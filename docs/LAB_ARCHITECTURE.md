# Analysis Lab Architecture

## Target scope

The complete lab combines Windows and Linux analysis, host telemetry, simulated networking, memory forensics and detection testing. The initial Python tool is one component, not the scope limit.

## Virtual machines

- Windows analysis guest: FLARE-VM, Ghidra, x64dbg, Sysinternals tools, Wireshark, capa, FLOSS and YARA.
- Linux analysis guest: REMnux, Ghidra, GDB, binutils and Python.
- Optional telemetry guest: logging and detection validation after basic containment is proven.

Target planning allocations: 8 GB RAM per primary guest with room for the host; increase for memory dumps and simultaneous workloads. Tool minimums and compatibility change: use each vendor's current documentation when provisioning.

## Isolation and snapshots

Use a hypervisor internal virtual network with no route to the host, home/campus LAN or Internet during analysis. Host-only networks can expose the host and are not equivalent to isolated internal networks. Avoid bridged networking. Disable shared folders, clipboard sharing, drag-and-drop and unnecessary USB passthrough for analysis guests.

Install and update official tools in a clean provisioning stage. Then disconnect external networking, snapshot the known-clean state and verify isolation before any untrusted execution. Any vendor instructions to reduce guest protections apply only to a disposable lab guest, never the daily host.

Use simulated services inside the lab where needed. Packet captures should remain inside the isolated lab. A VM is a containment layer, not an absolute guarantee against escape.

## Workflow artifacts

Record VM image identifiers, tool versions, snapshot name, sample hash, network mode, evidence hashes and UTC timestamps. Preserve original evidence separately from working copies. Revert the analysis guest after each case.

## Release criteria

A lab is ready for controlled dynamic exercises only after networking and host integration checks, clean snapshot recovery and evidence collection have been demonstrated. Do not describe this repository alone as a fully provisioned lab.
