#pip install pytest-watch
ptw --onpass "echo -e '---- OK ----\a'" --onfail "echo -e 'XXXX ERROR XXXX\a\a\a'"
