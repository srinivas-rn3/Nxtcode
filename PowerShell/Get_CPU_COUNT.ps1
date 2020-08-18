Connect-VIServer -Server sft041x0005.itci.softwaregrp.net -Protocol https -User svc_hcm-vcenter-dev -Password fInVu4!sWG9y
Function Get-HostCPUInfo {
	Param(
		[Parameter(Position=0, ValueFromPipeline=$true, Mandatory=$true)][String]$vmHost
	)
    
    $server = get-VMHost $vmHost

	$object = New-Object -TypeName PSObject
	$object | Add-Member -type NoteProperty -name HostName -value $server.Name
	$object | Add-Member -type NoteProperty -name ClusterName -value $server.cluster
    $object| Add-Member -type NoteProperty -name CpuMhz -value $server.ExtensionData.summary.hardware.CpuMhz
    $object| Add-Member -type NoteProperty -name NumCpuPkgs -value $server.ExtensionData.summary.hardware.NumCpuPkgs
    $object| Add-Member -type NoteProperty -name CpuCores -value $server.ExtensionData.summary.hardware.NumCpuCores
    $object| Add-Member -type NoteProperty -name CpuThreds -value $server.ExtensionData.summary.hardware.NumCpuThreads
    Return ($object)
}

# add the PowerClI VMware snapins
# Add-PSSnapin vmware*

# Connect to the vCenter server
# $vCenter = Read-Host "Enter your vCenter server name"
# $Connect-VIServer $vCenter

# Get a list of vmware hosts
$vmHostList = Get-VMHost

$output = @()
foreach ($vmHost in $vmHostList) {
   $output += Get-HostCPUInfo -vmHost $vmHost.name #| select hostname, CpuSockets, CpuCores
}
$output | ft
