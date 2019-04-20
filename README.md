Repo used to manage a storage instance provided by vultr

0. Make sure we have ansible installed.


1. Create/Reinstall a storage instance from web console, then run this command:

```
ansible-playbook -i 45.32.92.26, init.yml --user root --ask-pass -vvv
```

When prompted, paste the root password from vultr.

2. Run the following command to configure the instance:

```
./run 45.32.92.26
```

3. Credentials used in the setup process are passed in via environment variables. We should expect a `.env` file in the current directory that looks like this:

```
export RPC_USER='username'
export RPC_PASS='password'
export Namesilo_Key='apikey'
```
