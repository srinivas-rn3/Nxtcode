&nbsp;

$outputFile = "C:\CPU-Memory-Ratio.csv"
$VC = "vCenter Name"

##Connect to the vCenter
Connect-VIServer $VC -User "test" -Password "test"

$Output =@()

Get-Cluster | %{
$hypCluster = $_

## get the GenericMeasureInfo for the desired properties for this cluster's hosts
$infoCPUMEM = Get-View -ViewType HostSystem -Property Hardware.CpuInfo,Hardware.memorysize -SearchRoot $hypCluster.Id |
Select @{n="NumCpuSockets"; e={$_.Hardware.CpuInfo.NumCpuPackages}}, @{n="NumCpuCores"; e={$_.Hardware.CpuInfo.NumCpuCores}}, @{n="NumCpuThreads"; e={$_.Hardware.CpuInfo.NumCpuThreads}},@{n="PhysicalMem"; E={""+[math]::round($_.Hardware.MemorySize / 1GB, 0)}} |
Measure-Object -Sum NumCpuSockets,NumCpuCores,NumCpuThreads,PhysicalMem

## return an object with info about VMHosts' CPU characteristics

$temp= New-Object psobject
$datacenter = Get-Datacenter -Cluster $hypCluster.Name
$NumVMHosts = if ($infoCPUMEM) {$infoCPUMEM[0].Count} else {0}
$NumCpuSockets = ($infoCPUMEM | ?{$_.Property -eq "NumCpuSockets"}).Sum
$NumCpuCores = ($infoCPUMEM | ?{$_.Property -eq "NumCpuCores"}).Sum
$vmdetails = Get-VM -Location $hypCluster
$NumvCPU = ( $vmdetails | Measure-Object NumCpu -Sum).Sum
$VirtualMem= [Math]::Round(($vmdetails | Measure-Object MemoryGB -Sum).Sum, 2)
$PhysicalMem = ($infoCPUMEM | ?{$_.Property -eq "PhysicalMem"}).Sum

##Calculating the vCPU to pCPU ratio AND vRAM to pRAM ratio.

if ($NumvCPU -ne "0") {$cpuRatio= "$("{0:N2}" -f ($NumvCPU/$NumCpuCores))" + ":1"}
if ($VirtualMem -ne "0") {$memRatio= "$("{0:N2}" -f ($VirtualMem/$PhysicalMem))" + ":1"}

$temp | Add-Member -MemberType Noteproperty "Datacenter" -Value $datacenter
$temp | Add-Member -MemberType Noteproperty "ClusterName" -Value $hypCluster.Name
$temp | Add-Member -MemberType Noteproperty "NumVMHosts" -Value $NumVMHosts
$temp | Add-Member -MemberType Noteproperty "NumPCPUSockets" -Value $NumCpuSockets
$temp | Add-Member -MemberType Noteproperty "NumPCPUCores" -Value $NumCpuCores
$temp | Add-Member -MemberType Noteproperty "NumvCPU" -Value $NumvCPU
$temp | Add-Member -MemberType Noteproperty "vCPU-pCPUCoreRatio" -Value $cpuRatio
$temp | Add-Member -MemberType Noteproperty "PhysicalMem(GB)" -Value $PhysicalMem
$temp | Add-Member -MemberType Noteproperty "VirtualMem(GB)" -Value $VirtualMem
$temp | Add-Member -MemberType Noteproperty "vRAM-pRAMRatio" -Value $memRatio

$Output+=$temp

}
$Output | Sort-Object Account | Export-Csv -NoTypeInformation $outputFile
