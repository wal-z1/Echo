import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";
import Chatroom from "./Chatroom";

function ChatroomWrapper() {
	const { room, user } = useParams();
	return <Chatroom room={room} user={user} />;
}

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route
					path="/chat/:room/:user"
					element={
						<>
							<h1 className="text-4xl font-bold font-inter text-white mb-8 text-center drop-shadow-lg">
								ECHO Chat Room
							</h1>
							<ChatroomWrapper />
						</>
					}
				/>
			</Routes>
		</BrowserRouter>
	);
}
