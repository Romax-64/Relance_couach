{% if is_fr %}
<strong>{{ sender_name }}</strong><br>
Département logistique
<p><img src="cid:{{ logo_cid }}" alt="Logo"></p>
Chantier Naval Couach<br>
Email: {{ settings.SENDER_EMAIL }}
{% else %}
<strong>{{ sender_name }}</strong><br>
Logistical Department
<p><img src="cid:{{ logo_cid }}" alt="Logo"></p>
Couach Naval Shipyard<br>
Email: {{ settings.SENDER_EMAIL }}
{% endif %}