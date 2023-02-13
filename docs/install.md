# Install


## Python Virtual environment

```console
$ cd ${SNFF}
$ python3 -m venv .venv
$ source .venv/bin/activate
```


## Update Pip
```console
$ pip3 install -U pip wheel
Requirement already satisfied: pip in ./.venv/lib/python3.10/site-packages (23.0)
Collecting wheel
  Using cached wheel-0.38.4-py3-none-any.whl (36 kB)
Installing collected packages: wheel
Successfully installed wheel-0.38.4
```

## Instal Jupyter Lab

```console
$ pip3 install jupyterlab
Collecting jupyterlab
  Downloading jupyterlab-3.6.1-py3-none-any.whl (8.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 33.8 MB/s eta 0:00:00
Collecting jinja2>=2.1
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting nbclassic
  Downloading nbclassic-0.5.1-py3-none-any.whl (10.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.0/10.0 MB 35.1 MB/s eta 0:00:00
Collecting ipython
  Downloading ipython-8.10.0-py3-none-any.whl (784 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 784.3/784.3 kB 18.1 MB/s eta 0:00:00
Collecting packaging
  Using cached packaging-23.0-py3-none-any.whl (42 kB)
Collecting jupyter-server<3,>=1.16.0
  Downloading jupyter_server-2.2.1-py3-none-any.whl (365 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 365.3/365.3 kB 12.4 MB/s eta 0:00:00
Collecting tomli
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting jupyter-ydoc~=0.2.2
  Downloading jupyter_ydoc-0.2.2-py3-none-any.whl (5.6 kB)
Collecting jupyterlab-server~=2.19
  Using cached jupyterlab_server-2.19.0-py3-none-any.whl (56 kB)
Collecting jupyter-server-ydoc<0.7.0,>=0.6.0
  Downloading jupyter_server_ydoc-0.6.1-py3-none-any.whl (11 kB)
Collecting jupyter-core
  Downloading jupyter_core-5.2.0-py3-none-any.whl (94 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 94.3/94.3 kB 3.9 MB/s eta 0:00:00
Collecting notebook<7
  Using cached notebook-6.5.2-py3-none-any.whl (439 kB)
Collecting tornado>=6.1.0
  Using cached tornado-6.2-cp37-abi3-macosx_10_9_x86_64.whl (419 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.1.2-cp310-cp310-macosx_10_9_x86_64.whl (13 kB)
Collecting traitlets>=5.6.0
  Downloading traitlets-5.9.0-py3-none-any.whl (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.4/117.4 kB 4.5 MB/s eta 0:00:00
Collecting nbconvert>=6.4.4
  Downloading nbconvert-7.2.9-py3-none-any.whl (274 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 274.9/274.9 kB 10.1 MB/s eta 0:00:00
Collecting anyio>=3.1.0
  Using cached anyio-3.6.2-py3-none-any.whl (80 kB)
Collecting jupyter-server-terminals
  Using cached jupyter_server_terminals-0.4.4-py3-none-any.whl (13 kB)
Collecting websocket-client
  Downloading websocket_client-1.5.1-py3-none-any.whl (55 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.9/55.9 kB 2.0 MB/s eta 0:00:00
Collecting pyzmq>=24
  Using cached pyzmq-25.0.0-cp310-cp310-macosx_10_15_universal2.whl (1.8 MB)
Collecting jupyter-client>=7.4.4
  Downloading jupyter_client-8.0.2-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 4.0 MB/s eta 0:00:00
Collecting terminado>=0.8.3
  Using cached terminado-0.17.1-py3-none-any.whl (17 kB)
Collecting prometheus-client
  Using cached prometheus_client-0.16.0-py3-none-any.whl (122 kB)
Collecting nbformat>=5.3.0
  Using cached nbformat-5.7.3-py3-none-any.whl (78 kB)
Collecting jupyter-events>=0.4.0
  Using cached jupyter_events-0.6.3-py3-none-any.whl (18 kB)
Collecting send2trash
  Using cached Send2Trash-1.8.0-py3-none-any.whl (18 kB)
Collecting argon2-cffi
  Using cached argon2_cffi-21.3.0-py3-none-any.whl (14 kB)
Collecting platformdirs>=2.5
  Downloading platformdirs-3.0.0-py3-none-any.whl (14 kB)
Collecting ypy-websocket<0.9.0,>=0.8.2
  Downloading ypy_websocket-0.8.2-py3-none-any.whl (10 kB)
Collecting jupyter-server-fileid<1,>=0.6.0
  Downloading jupyter_server_fileid-0.6.0-py3-none-any.whl (15 kB)
Collecting y-py<0.6.0,>=0.5.3
  Downloading y_py-0.5.5-cp310-cp310-macosx_10_9_x86_64.macosx_11_0_arm64.macosx_10_9_universal2.whl (1.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 24.2 MB/s eta 0:00:00
Collecting json5>=0.9.0
  Using cached json5-0.9.11-py2.py3-none-any.whl (19 kB)
Collecting requests>=2.28
  Using cached requests-2.28.2-py3-none-any.whl (62 kB)
Collecting babel>=2.10
  Using cached Babel-2.11.0-py3-none-any.whl (9.5 MB)
Collecting jsonschema>=4.17.3
  Using cached jsonschema-4.17.3-py3-none-any.whl (90 kB)
Collecting ipykernel
  Downloading ipykernel-6.21.1-py3-none-any.whl (149 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.8/149.8 kB 5.7 MB/s eta 0:00:00
Collecting nest-asyncio>=1.5
  Using cached nest_asyncio-1.5.6-py3-none-any.whl (5.2 kB)
Collecting ipython-genutils
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting notebook-shim>=0.1.0
  Using cached notebook_shim-0.2.2-py3-none-any.whl (13 kB)
Collecting stack-data
  Using cached stack_data-0.6.2-py3-none-any.whl (24 kB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting jedi>=0.16
  Using cached jedi-0.18.2-py2.py3-none-any.whl (1.6 MB)
Collecting decorator
  Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting pygments>=2.4.0
  Using cached Pygments-2.14.0-py3-none-any.whl (1.1 MB)
Collecting appnope
  Using cached appnope-0.1.3-py2.py3-none-any.whl (4.4 kB)
Collecting prompt-toolkit<3.1.0,>=3.0.30
  Using cached prompt_toolkit-3.0.36-py3-none-any.whl (386 kB)
Collecting pexpect>4.3
  Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
Collecting matplotlib-inline
  Using cached matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting idna>=2.8
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting sniffio>=1.1
  Using cached sniffio-1.3.0-py3-none-any.whl (10 kB)
Collecting pytz>=2015.7
  Using cached pytz-2022.7.1-py2.py3-none-any.whl (499 kB)
Collecting parso<0.9.0,>=0.8.0
  Using cached parso-0.8.3-py2.py3-none-any.whl (100 kB)
Collecting attrs>=17.4.0
  Using cached attrs-22.2.0-py3-none-any.whl (60 kB)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Using cached pyrsistent-0.19.3-cp310-cp310-macosx_10_9_universal2.whl (82 kB)
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting python-json-logger>=2.0.4
  Downloading python_json_logger-2.0.5-py3-none-any.whl (7.8 kB)
Collecting rfc3339-validator
  Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Collecting pyyaml>=5.3
  Using cached PyYAML-6.0-cp310-cp310-macosx_10_9_x86_64.whl (197 kB)
Collecting rfc3986-validator>=0.1.1
  Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Collecting jupyter-events>=0.4.0
  Downloading jupyter_events-0.5.0-py3-none-any.whl (17 kB)
Collecting mistune<3,>=2.0.3
  Downloading mistune-2.0.5-py2.py3-none-any.whl (24 kB)
Collecting nbclient>=0.5.0
  Using cached nbclient-0.7.2-py3-none-any.whl (71 kB)
Collecting bleach
  Using cached bleach-6.0.0-py3-none-any.whl (162 kB)
Collecting jupyterlab-pygments
  Using cached jupyterlab_pygments-0.2.2-py2.py3-none-any.whl (21 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.11.2-py3-none-any.whl (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.4/129.4 kB 5.4 MB/s eta 0:00:00
Collecting defusedxml
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Collecting tinycss2
  Using cached tinycss2-1.2.1-py3-none-any.whl (21 kB)
Collecting pandocfilters>=1.4.1
  Using cached pandocfilters-1.5.0-py2.py3-none-any.whl (8.7 kB)
Collecting fastjsonschema
  Using cached fastjsonschema-2.16.2-py3-none-any.whl (22 kB)
Collecting ptyprocess>=0.5
  Using cached ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.6-py2.py3-none-any.whl (29 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.14-py2.py3-none-any.whl (140 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2022.12.7-py3-none-any.whl (155 kB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.0.1-cp310-cp310-macosx_10_9_x86_64.whl (124 kB)
Collecting aiofiles<23,>=22.1.0
  Downloading aiofiles-22.1.0-py3-none-any.whl (14 kB)
Collecting aiosqlite<1,>=0.17.0
  Downloading aiosqlite-0.18.0-py3-none-any.whl (15 kB)
Collecting argon2-cffi-bindings
  Using cached argon2_cffi_bindings-21.2.0-cp38-abi3-macosx_10_9_universal2.whl (53 kB)
Collecting psutil
  Using cached psutil-5.9.4-cp36-abi3-macosx_10_9_x86_64.whl (243 kB)
Collecting comm>=0.1.1
  Using cached comm-0.1.2-py3-none-any.whl (6.5 kB)
Collecting debugpy>=1.6.5
  Using cached debugpy-1.6.6-cp310-cp310-macosx_11_0_x86_64.whl (1.7 MB)
Collecting pure-eval
  Using cached pure_eval-0.2.2-py3-none-any.whl (11 kB)
Collecting asttokens>=2.1.0
  Using cached asttokens-2.2.1-py2.py3-none-any.whl (26 kB)
Collecting executing>=1.2.0
  Using cached executing-1.2.0-py2.py3-none-any.whl (24 kB)
Collecting six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting fqdn
  Using cached fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Collecting isoduration
  Using cached isoduration-20.11.0-py3-none-any.whl (11 kB)
Collecting uri-template
  Using cached uri_template-1.2.0-py3-none-any.whl (10 kB)
Collecting webcolors>=1.11
  Using cached webcolors-1.12-py3-none-any.whl (9.9 kB)
Collecting jsonpointer>1.13
  Using cached jsonpointer-2.3-py2.py3-none-any.whl (7.8 kB)
Collecting cffi>=1.0.1
  Using cached cffi-1.15.1-cp310-cp310-macosx_10_9_x86_64.whl (179 kB)
Collecting soupsieve>1.2
  Using cached soupsieve-2.3.2.post1-py3-none-any.whl (37 kB)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Collecting arrow>=0.15.0
  Using cached arrow-1.2.3-py3-none-any.whl (66 kB)
Installing collected packages: y-py, webencodings, wcwidth, send2trash, pytz, pure-eval, ptyprocess, pickleshare, mistune, json5, ipython-genutils, fastjsonschema, executing, charset-normalizer, backcall, appnope, websocket-client, webcolors, urllib3, uri-template, traitlets, tornado, tomli, tinycss2, soupsieve, sniffio, six, rfc3986-validator, pyzmq, pyyaml, python-json-logger, pyrsistent, pygments, pycparser, psutil, prompt-toolkit, prometheus-client, platformdirs, pexpect, parso, pandocfilters, packaging, nest-asyncio, MarkupSafe, jupyterlab-pygments, jupyter-ydoc, jsonpointer, idna, fqdn, defusedxml, decorator, debugpy, certifi, babel, attrs, aiosqlite, aiofiles, ypy-websocket, terminado, rfc3339-validator, requests, python-dateutil, matplotlib-inline, jupyter-core, jsonschema, jinja2, jedi, comm, cffi, bleach, beautifulsoup4, asttokens, anyio, stack-data, nbformat, jupyter-server-terminals, jupyter-client, arrow, argon2-cffi-bindings, nbclient, isoduration, ipython, argon2-cffi, nbconvert, ipykernel, jupyter-events, jupyter-server, notebook-shim, jupyterlab-server, jupyter-server-fileid, nbclassic, jupyter-server-ydoc, notebook, jupyterlab
Successfully installed MarkupSafe-2.1.2 aiofiles-22.1.0 aiosqlite-0.18.0 anyio-3.6.2 appnope-0.1.3 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 arrow-1.2.3 asttokens-2.2.1 attrs-22.2.0 babel-2.11.0 backcall-0.2.0 beautifulsoup4-4.11.2 bleach-6.0.0 certifi-2022.12.7 cffi-1.15.1 charset-normalizer-3.0.1 comm-0.1.2 debugpy-1.6.6 decorator-5.1.1 defusedxml-0.7.1 executing-1.2.0 fastjsonschema-2.16.2 fqdn-1.5.1 idna-3.4 ipykernel-6.21.1 ipython-8.10.0 ipython-genutils-0.2.0 isoduration-20.11.0 jedi-0.18.2 jinja2-3.1.2 json5-0.9.11 jsonpointer-2.3 jsonschema-4.17.3 jupyter-client-8.0.2 jupyter-core-5.2.0 jupyter-events-0.5.0 jupyter-server-2.2.1 jupyter-server-fileid-0.6.0 jupyter-server-terminals-0.4.4 jupyter-server-ydoc-0.6.1 jupyter-ydoc-0.2.2 jupyterlab-3.6.1 jupyterlab-pygments-0.2.2 jupyterlab-server-2.19.0 matplotlib-inline-0.1.6 mistune-2.0.5 nbclassic-0.5.1 nbclient-0.7.2 nbconvert-7.2.9 nbformat-5.7.3 nest-asyncio-1.5.6 notebook-6.5.2 notebook-shim-0.2.2 packaging-23.0 pandocfilters-1.5.0 parso-0.8.3 pexpect-4.8.0 pickleshare-0.7.5 platformdirs-3.0.0 prometheus-client-0.16.0 prompt-toolkit-3.0.36 psutil-5.9.4 ptyprocess-0.7.0 pure-eval-0.2.2 pycparser-2.21 pygments-2.14.0 pyrsistent-0.19.3 python-dateutil-2.8.2 python-json-logger-2.0.5 pytz-2022.7.1 pyyaml-6.0 pyzmq-25.0.0 requests-2.28.2 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 send2trash-1.8.0 six-1.16.0 sniffio-1.3.0 soupsieve-2.3.2.post1 stack-data-0.6.2 terminado-0.17.1 tinycss2-1.2.1 tomli-2.0.1 tornado-6.2 traitlets-5.9.0 uri-template-1.2.0 urllib3-1.26.14 wcwidth-0.2.6 webcolors-1.12 webencodings-0.5.1 websocket-client-1.5.1 y-py-0.5.5 ypy-websocket-0.8.2
```


## Run Jupyter lab

```console
jupyter lab --notebook-dir snff/notebook
[I 2023-02-13 14:30:04.282 ServerApp] Package jupyterlab took 0.0000s to import
[I 2023-02-13 14:30:04.284 ServerApp] Package jupyter_server_fileid took 0.0020s to import
[I 2023-02-13 14:30:04.288 ServerApp] Package jupyter_server_terminals took 0.0040s to import
[I 2023-02-13 14:30:04.304 ServerApp] Package jupyter_server_ydoc took 0.0149s to import
[I 2023-02-13 14:30:04.304 ServerApp] Package nbclassic took 0.0000s to import
[W 2023-02-13 14:30:04.305 ServerApp] A `_jupyter_server_extension_points` function was not found in nbclassic. Instead, a `_jupyter_server_extension_paths` function was found and will be used for now. This function name will be deprecated in future releases of Jupyter Server.
[I 2023-02-13 14:30:04.306 ServerApp] Package notebook_shim took 0.0000s to import
[W 2023-02-13 14:30:04.306 ServerApp] A `_jupyter_server_extension_points` function was not found in notebook_shim. Instead, a `_jupyter_server_extension_paths` function was found and will be used for now. This function name will be deprecated in future releases of Jupyter Server.
[I 2023-02-13 14:30:04.310 ServerApp] jupyter_server_fileid | extension was successfully linked.
[I 2023-02-13 14:30:04.313 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2023-02-13 14:30:04.316 ServerApp] jupyter_server_ydoc | extension was successfully linked.
[I 2023-02-13 14:30:04.320 ServerApp] jupyterlab | extension was successfully linked.
[I 2023-02-13 14:30:04.324 ServerApp] nbclassic | extension was successfully linked.
[I 2023-02-13 14:30:04.490 ServerApp] notebook_shim | extension was successfully linked.
[I 2023-02-13 14:30:04.620 ServerApp] notebook_shim | extension was successfully loaded.
[I 2023-02-13 14:30:04.620 FileIdExtension] Configured File ID manager: ArbitraryFileIdManager
[I 2023-02-13 14:30:04.621 FileIdExtension] ArbitraryFileIdManager : Configured root dir: /Users/cees/Projects/snff/snff/notebook
[I 2023-02-13 14:30:04.621 FileIdExtension] ArbitraryFileIdManager : Configured database path: /Users/cees/Library/Jupyter/file_id_manager.db
[I 2023-02-13 14:30:04.621 FileIdExtension] ArbitraryFileIdManager : Successfully connected to database file.
[I 2023-02-13 14:30:04.621 FileIdExtension] ArbitraryFileIdManager : Creating File ID tables and indices.
[I 2023-02-13 14:30:04.622 FileIdExtension] Attached event listeners.
[I 2023-02-13 14:30:04.622 ServerApp] jupyter_server_fileid | extension was successfully loaded.
[I 2023-02-13 14:30:04.623 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2023-02-13 14:30:04.623 ServerApp] jupyter_server_ydoc | extension was successfully loaded.
[I 2023-02-13 14:30:04.624 LabApp] JupyterLab extension loaded from /Users/cees/Projects/snff/.venv/lib/python3.10/site-packages/jupyterlab
[I 2023-02-13 14:30:04.624 LabApp] JupyterLab application directory is /Users/cees/Projects/snff/.venv/share/jupyter/lab
[I 2023-02-13 14:30:04.626 ServerApp] jupyterlab | extension was successfully loaded.
[I 2023-02-13 14:30:04.629 ServerApp] nbclassic | extension was successfully loaded.
[I 2023-02-13 14:30:04.630 ServerApp] Serving notebooks from local directory: /Users/cees/Projects/snff/snff/notebook
[I 2023-02-13 14:30:04.630 ServerApp] Jupyter Server 2.2.1 is running at:
[I 2023-02-13 14:30:04.630 ServerApp] http://localhost:8888/lab?token=57279a04507c739ae8a9c733e80231f87e6c4b02e2d2e2d1
[I 2023-02-13 14:30:04.630 ServerApp]     http://127.0.0.1:8888/lab?token=57279a04507c739ae8a9c733e80231f87e6c4b02e2d2e2d1
[I 2023-02-13 14:30:04.630 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2023-02-13 14:30:04.638 ServerApp]

    To access the server, open this file in a browser:
        file:///Users/cees/Library/Jupyter/runtime/jpserver-26463-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=57279a04507c739ae8a9c733e80231f87e6c4b02e2d2e2d1
        http://127.0.0.1:8888/lab?token=57279a04507c739ae8a9c733e80231f87e6c4b02e2d2e2d1
[I 2023-02-13 14:30:07.707 LabApp] Build is up to date

```