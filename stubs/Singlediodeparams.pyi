class SingleDiodeModel(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	Adj_ref = float
	I = float
	Il_ref = float
	Io_ref = float
	Rs_ref = float
	Rsh_ref = float
	T = float
	a_ref = float
	alpha_isc = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	Il = float
	Io = float
	Rs = float
	Rsh = float
	a = float


class Singlediodeparams(object):
	def assign(self, dict):
		pass

	def value(self, name, value=None):
		pass

	def execute(self, int_verbosity):
		pass

	def export(self):
		pass

	def __getattribute__(self, *args, **kwargs):
		pass

	def __init__(self, *args, **kwargs):
		pass

	SingleDiodeModel = SingleDiodeModel
	Outputs = Outputs


def default(config) -> Singlediodeparams
	pass

def new() -> Singlediodeparams
	pass

def wrap(ssc_data_t) -> Singlediodeparams
	pass

def from_existing(model, config="") -> Singlediodeparams
	pass

__loader__ = None 

__spec__ = None
