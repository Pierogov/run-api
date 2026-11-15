<h1>Run-api</h1>
<p><i>Simple Flask Api used to store and return your PRs for most popular running distances</i></p>
<br>
<h2>Quick start</h2>
<p>Files are stored in times folder (in docker image stored as a volume) - 5.txt, 10.txt, 21.txt, 42.txt files containing only time in hh:mm:ss format</p>
<p>/api/run/{distance} - endpoint used to read data</p>
<p>/api/run/update/{distance}?time=hh:mm:ss - endpoint used to write new time to file</p>
<h2>Deployment using docker</h2>
<p>Just paste these commands and everything should be running. Default app port is <b>5000</b>.</p>

```
git clone https://github.com/Pierogov/run-api.git
cd run-api/
docker compose up -d
```
