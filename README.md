# macos_keychain

MacOS keychain password manager

## Adding a password to keychain

```python
import macos_keychain

macos_keychain.add(name='API token', value='<TOKEN>')
```

## Removing passwords in keychain

```python
import macos_keychain

macos_keychain.rm(name='API token')
```

## Listing passwords in keychain

```python
import macos_keychain

macos_keychain.ls()
```

## Getting password in keychain
```python
import macos_keychain

macos_keychain.get(name='API token')
```
