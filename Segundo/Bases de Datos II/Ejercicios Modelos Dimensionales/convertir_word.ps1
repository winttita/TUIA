# Crear objeto de aplicación Word
$word_app = New-Object -ComObject Word.Application
$word_app.Visible = $false

# Obtener todos los archivos Word en el directorio actual
$files = Get-ChildItem -Path . -Include *.doc, *.docx -Recurse

foreach ($file in $files) {
    Write-Host "Convirtiendo: $($file.Name)..." -ForegroundColor Cyan
    
    # Definir la ruta de salida (cambiando la extensión)
    $pdf_path = $file.FullName -replace '\.docx?$', '.pdf'
    
    # Abrir el documento y guardarlo como PDF (Format 17)
    $doc = $word_app.Documents.Open($file.FullName)
    $doc.SaveAs([ref] $pdf_path, [ref] 17)
    $doc.Close()
}

# Cerrar Word y limpiar memoria
$word_app.Quit()
Write-Host "Proceso finalizado con éxito." -ForegroundColor Green