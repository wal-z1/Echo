import Chatroom from "./Chatroom";
function App() {
	return (
		<>
			<div className=" grid grid-rows-2 gap-3 ">
				<h1 className="text-3xl font-bold underline font-mozilla mx-auto text-[#F5F5F5]">
					Simple FrontEnd For ECHO chat room
				</h1>
				<Chatroom />
			</div>
		</>
	);
}

export default App;
