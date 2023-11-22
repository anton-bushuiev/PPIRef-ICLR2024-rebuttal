from typing import Union, Iterable
from pathlib import Path


NOPPI_EXTENSION: str = '.noppi'


# TODO Check for the absence of '_' symbols in input paths
class PPIPath(type(Path())):
    def __new__(cls, *args, **kwargs):  # https://stackoverflow.com/q/61689391
        obj = super().__new__(cls, *args, **kwargs)
        if obj.suffix not in ['.pdb', NOPPI_EXTENSION]:
            raise ValueError(f'Wrong PPI file extension {obj.suffix}.')
        return obj        

    def is_dummy(self) -> bool:
        return self.suffix == NOPPI_EXTENSION
    
    def ppi_id(self) -> str:
        return path_to_ppi_id(self)

    def pdb_id(self) -> str:
        return path_to_pdb_id(self)

    def partners(self) -> list[str]:
        return path_to_partners(self)
    
    def is_equivalent_to(self, other: Union[Path, str]) -> bool:
        other = PPIPath(other)
        return (
            self.pdb_id() == other.pdb_id() and
            set(self.partners()) == set(other.partners())
        )

    def contains(self, other: Union[Path, str]) -> bool:
        other = PPIPath(other)
        return (
            self.pdb_id() == other.pdb_id() and
            set(self.partners()) >= set(other.partners())
        )

    def with_sorted_partners(self) -> Path:
        return self.with_stem(self.pdb_id() + '_' + '_'.join(sorted(self.partners())))


# Functional API

def path_to_ppi_id(path: Union[Path, str]) -> str:
    stem = Path(path).stem
    if stem[0] == '.':  # hidden file
        stem = stem[1:]
    return stem.split('.', 1)[0]


def path_to_pdb_id(path: Union[Path, str]) -> str:
    return path_to_ppi_id(path).split('_')[0]


def path_to_partners(path: Union[Path, str]) -> list:
    return path_to_ppi_id(path).split('_')[1:]


def pdb_id_to_nested_suffix(pdb_id: str) -> str:
    return f'{pdb_id[1:3]}/{pdb_id}.pdb'


def ppi_id_to_nested_suffix(ppi_id: str) -> str:
    return pdb_id_to_nested_suffix(ppi_id)  # Works same
