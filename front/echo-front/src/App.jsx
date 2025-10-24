import Chatroom from "./Chatroom";

function App() {
	return (
		<div className="min-h-screen flex flex-col items-center justify-center px-4 py-8">
			<h1 className="text-4xl font-bold font-inter text-white mb-8 text-center drop-shadow-lg">
				Simple Front-End For ECHO Chat Room
			</h1>
			<Chatroom />
		</div>
	);
}

export default App;
