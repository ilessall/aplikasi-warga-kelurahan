document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('warga-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            container.innerHTML = '';

            data.results.forEach(warga => {
                const div = document.createElement('div');
                div.style.border = '1px solid #ccc';
                div.style.margin = '10px';
                div.style.padding = '10px';

                div.innerHTML = `
                    <h3>${warga.nama_lengkap}</h3>
                    <p>NIK: ${warga.nik}</p>
                    <p>Alamat: ${warga.alamat}</p>
                `;

                container.appendChild(div);
            });
        })
        .catch(error => {
            container.innerHTML = 'Gagal memuat data';
            console.error(error);
        });

        const form = document.getElementById('warga-form');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const data = {
        nik: document.getElementById('nik').value,
        nama_lengkap: document.getElementById('nama').value,
        alamat: document.getElementById('alamat').value,
        no_telepon: document.getElementById('telepon').value
    };

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(() => {
        alert('Data berhasil disimpan');
        location.reload(); // refresh data
    })
    .catch(error => console.error(error));
});

});
