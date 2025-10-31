// JavaScript personalizado para la aplicación de Redes OSI

// Función para inicializar la aplicación
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Aplicación de Redes OSI iniciada');
    
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Inicializar popovers de Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Agregar animaciones a las cards
    animateCards();
    
    // Configurar validación de formularios
    setupFormValidation();
    
    // Configurar efectos de hover
    setupHoverEffects();
    
    // Configurar auto-hide para alertas
    setupAlertAutoHide();
});

// Función para animar las cards
function animateCards() {
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, {
        threshold: 0.1
    });
    
    cards.forEach(card => {
        observer.observe(card);
    });
}

// Función para configurar validación de formularios
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// Función para configurar efectos de hover
function setupHoverEffects() {
    // Efecto de hover para botones
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Efecto de hover para cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
        });
    });
}

// Función para configurar auto-hide de alertas
function setupAlertAutoHide() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Auto-hide después de 5 segundos
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

// Función para mostrar notificaciones
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-hide después de 3 segundos
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 3000);
}

// Función para confirmar eliminación
function confirmDelete(message = '¿Estás seguro de que quieres eliminar este elemento?') {
    return confirm(message);
}

// Función para formatear fechas
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Función para truncar texto
function truncateText(text, maxLength = 100) {
    if (text.length <= maxLength) {
        return text;
    }
    return text.substring(0, maxLength) + '...';
}

// Función para validar formularios en tiempo real
function setupRealTimeValidation() {
    const inputs = document.querySelectorAll('input[required], textarea[required], select[required]');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            if (this.classList.contains('is-invalid')) {
                validateField(this);
            }
        });
    });
}

// Función para validar un campo específico
function validateField(field) {
    const value = field.value.trim();
    const isValid = value.length > 0;
    
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
    }
}

// Función para copiar al portapapeles
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Texto copiado al portapapeles', 'success');
    }).catch(err => {
        console.error('Error al copiar: ', err);
        showNotification('Error al copiar al portapapeles', 'danger');
    });
}

// Función para exportar tabla a CSV
function exportTableToCSV(tableId, filename = 'protocolos.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    for (let i = 0; i < rows.length; i++) {
        const row = [], cols = rows[i].querySelectorAll('td, th');
        
        for (let j = 0; j < cols.length; j++) {
            // Obtener solo el texto, sin HTML
            let text = cols[j].innerText.replace(/"/g, '""');
            row.push('"' + text + '"');
        }
        
        csv.push(row.join(','));
    }
    
    // Descargar archivo
    const csvContent = csv.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    
    if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', filename);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

// Función para buscar en tablas
function setupTableSearch() {
    const searchInput = document.querySelector('#tableSearch');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const table = document.querySelector('.table');
        const rows = table.querySelectorAll('tbody tr');
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
}

// Función para ordenar tablas
function setupTableSorting() {
    const headers = document.querySelectorAll('th[data-sortable]');
    headers.forEach(header => {
        header.addEventListener('click', function() {
            const table = this.closest('table');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const columnIndex = Array.from(this.parentElement.children).indexOf(this);
            const isAscending = this.classList.contains('sort-asc');
            
            // Ordenar filas
            rows.sort((a, b) => {
                const aValue = a.children[columnIndex].textContent.trim();
                const bValue = b.children[columnIndex].textContent.trim();
                
                if (isAscending) {
                    return bValue.localeCompare(aValue);
                } else {
                    return aValue.localeCompare(bValue);
                }
            });
            
            // Actualizar tabla
            rows.forEach(row => tbody.appendChild(row));
            
            // Actualizar clases de ordenamiento
            headers.forEach(h => h.classList.remove('sort-asc', 'sort-desc'));
            this.classList.add(isAscending ? 'sort-desc' : 'sort-asc');
        });
    });
}

// Función para mostrar estadísticas en tiempo real
function updateStatistics() {
    const protocolos = document.querySelectorAll('tbody tr');
    const total = protocolos.length;
    
    // Actualizar contador total
    const totalElement = document.querySelector('#totalProtocolos');
    if (totalElement) {
        totalElement.textContent = total;
    }
    
    // Contar por capas
    const capas = {};
    protocolos.forEach(row => {
        const capaCell = row.querySelector('td:nth-child(4)');
        if (capaCell) {
            const capa = capaCell.textContent.trim();
            capas[capa] = (capas[capa] || 0) + 1;
        }
    });
    
    // Actualizar contadores por capa
    Object.keys(capas).forEach(capa => {
        const element = document.querySelector(`#${capa.replace(/\s+/g, '').toLowerCase()}`);
        if (element) {
            element.textContent = capas[capa];
        }
    });
}

// Inicializar funciones adicionales cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    setupRealTimeValidation();
    setupTableSearch();
    setupTableSorting();
    
    // Actualizar estadísticas si estamos en la página de protocolos
    if (window.location.pathname.includes('protocolos')) {
        updateStatistics();
    }
});

// Función para mostrar información de desarrollo
function showDevInfo() {
    console.log(`
    🌐 Aplicación de Redes OSI
    📁 Estructura del proyecto:
    ├── app.py (Aplicación principal Flask)
    ├── db/ (Base de datos)
    │   ├── conexion.py (Conexión MySQL)
    │   ├── gestiondb.py (Gestión de datos)
    │   └── redesiniciandoflask.sql (Script SQL)
    ├── templates/ (Plantillas HTML)
    │   ├── base.html (Plantilla base)
    │   ├── index.html (Página principal)
    │   └── protocolos.html (Gestión de protocolos)
    ├── static/ (Archivos estáticos)
    │   ├── css/style.css (Estilos personalizados)
    │   └── js/script.js (JavaScript personalizado)
    └── requirements.txt (Dependencias)
    
    🚀 Para ejecutar: python app.py
    📊 Base de datos: MySQL (redesiniciandoflask)
    🎨 Framework: Bootstrap 5 + Font Awesome
    `);
}

// Mostrar información de desarrollo en consola
showDevInfo(); 