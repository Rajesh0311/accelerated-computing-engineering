param(
    [ValidateSet("smoke", "full")]
    [string]$Mode = "smoke",

    [ValidateRange(0, 255)]
    [int]$Cpu = 0
)

$ErrorActionPreference = "Stop"

$experimentRoot = $PSScriptRoot
$repoRoot = (Resolve-Path "$experimentRoot\..\..").Path
$python = "C:\Users\rajes\gpu-perf-lab\venvs\ace-architecture\Scripts\python.exe"
$benchmark = Join-Path $experimentRoot "src\benchmark.py"
$results = Join-Path $experimentRoot "results"

if (-not (Test-Path -LiteralPath $python)) {
    throw "ACE architecture virtual environment was not found."
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$output = Join-Path $results "$Mode-$timestamp.csv"

Set-Location $repoRoot

& $python $benchmark `
    --mode $Mode `
    --cpu $Cpu `
    --output $output

if ($LASTEXITCODE -ne 0) {
    throw "Benchmark failed."
}
