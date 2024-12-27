# romSort
Sorts roms based on Region, then alphabatizes.

This was an AI-generated python script I asked chatGPT to make. Sharing it with the world for it to make use.
I would have tried to do it myself, but I still don't quite understand python myself.

Of course, this is slightly tailored to the way I wanted it, but still.

  - Region-Based Sorting for Numbers and Special Characters
  ROMs starting with numbers or special characters are now placed into folders labeled "1" (numbers) and "2" (special characters), nested under their respective region folders.
  
  - Dynamic Folder Creation
  The script dynamically organizes ROMs into a clear and hierarchical structure based on region and filename characteristics, improving organization and clarity.
---
**Enhanced with ChatGPT**

# Requirements
A set (or multiple sets) of roms.

```
├── romOrg.py
└── in
    ├── gba
        ├── bunchOfGbaRoms (USA).gba
        └── aSecondGbaRom (Europe).gba
    ├── nes
        ├── someNesRoms (Korea).nes
        └── 4-in-1 (U).nes
    └── gbc
        ├── $ (World).gbc
        └── 4-in-1 (Europe).gbc
```

Running romOrg.py (in this example) with in as the input dir and out as the output dir will return this:

```
├── romOrg.py
└── out
    ├── gba
        ├── USA
            ├── B
                └── bunchOfGbaRoms (USA).gba
        └── Europe
            └── A
                └── aSecondGbaRom (Europe).gba
    ├── nes
        ├── Korea
            └── S
                └── someNesRoms (Korea).nes
        └── USA
            └── 1
                └── 4-in-1 (U).nes
    ├── gbc
        ├── Other
            └── 2
                └── $ (World).gbc
        └── Europe
            └── 1
                └── 4-in-1 (Europe).gbc
```
